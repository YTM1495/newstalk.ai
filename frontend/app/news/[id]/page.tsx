import Link from "next/link";
type NewsArticle = {
    id: number;
    title: string;
    content: string;
    category: string;
    source: string;
    published_at : string;
};
type NewsPageProps = {
    params: {
        id: string;
    };
};
export default  async function NewsPage({
    params,
}:NewsPageProps)
{
const response  = await fetch(
    `http://localhost:8000/news/${params.id}`
);
if(!response.ok){
    throw new Error("Failed to fetch article");
}
const article: NewsArticle = await response.json();
return (
            <main>
        <h1>{article.title}</h1>
        <p>{article.category}</p>
        <p>{article.source}</p>
        <p>{article.published_at}</p>
        <p>{article.content}</p>
    </main>
    
    
    
)
}
