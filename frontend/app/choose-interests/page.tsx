"use client";

import { useEffect,useState } from "react";
import {useRouter} from "next/navigation";

type Category = {
    id:number;
    name:string;
};

export default function ChooseInterestPage(){
    const [categories, setCategories] = useState<Category[]>([]);
    const [selectedIds, setSelectedIds] = useState<number[]>([]);
    const [loading, setLoading] = useState(true);

    const router = useRouter();

    useEffect(() => {
        async function fetchCtegories(){
            try{
                const categoriesResponse = await fetch(
                    "http://127.0.0.1:8000/categories"
                );
                if(!categoriesResponse.ok){
                    throw new Error("Failed to fetch categories");
                }
                const categoriesData = await categoriesResponse.json();
                setCategories(categoriesData);

                const interestsResponse = await fetch(
                  "http://127.0.0.1:8000/users/1/interests"
                );

                if (!interestsResponse.ok){
                  throw new Error("Failed to fetch user interests");}

                const interestsData = await interestsResponse.json();

                const interestsIds = interestsData.map(
                  (category: Category) => category.id
                );
                setSelectedIds(interestsIds);
                
            }catch(error){
                console.log(error);
            }finally{
                setLoading(false);
            }
        }
        fetchCtegories();
    },[]);

    function toggleCategory(categoryId:number){
        setSelectedIds((current) => {
            if(current.includes(categoryId)){
                return current.filter((id) => id !== categoryId);
            }
            return [...current,categoryId];
        });
    }
    async function saveInterests() {
        if(selectedIds.length == 0){
            return;
        }
        try{
            const response = await fetch(
                "http://127.0.0.1:8000/users/1/interests",
                {
                    method: "POST",
                    headers: {
                    "Content-Type": "application/json", 
                },
                body: JSON.stringify({
                category_ids: selectedIds,
                }
            ),
        }
    );
    const data = await response.json();
    console.log("status:",response.status);
    console.log("Response:",JSON.stringify(data,null,2));
     if (!response.ok) {
        console.log("Backend error:", JSON.stringify(data, null, 2));
        throw new Error( "Failed to save interests");
    }
      router.push("/for-you");
    }catch(error){
        console.error(error);
    }}
    if(loading){
        return <p>Loading categories...</p>
    }
    return (
    <main className="max-w-3xl mx-auto p-6">

      <h1 className="text-3xl font-bold mb-2">
        Choose your interests
      </h1>

      <p className="text-gray-600 mb-6">
        Select the topics you want to see in your For You feed.
      </p>

      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">

        {categories.map((category) => {
          const selected = selectedIds.includes(category.id);

          return (
            <button
              key={category.id}
              onClick={() => toggleCategory(category.id)}
              className={`border rounded-lg p-4 text-left ${
                selected
                  ? "bg-black text-white"
                  : "bg-white text-black"
              }`}
            >
              {category.name}
            </button>
          );
        })}

      </div>

      <button
        onClick={saveInterests}
        disabled={selectedIds.length === 0}
        className="mt-8 px-6 py-3 rounded-lg bg-black text-white disabled:opacity-50"
      >
        Continue
      </button>

    </main>
  );
}