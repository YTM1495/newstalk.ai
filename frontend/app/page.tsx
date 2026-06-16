import NewsCard from "../components/NewsCard";
export default async function Home(){
        type NewsArticle = {
          id:number;
          title:string;
          category:string;
          source:string;
        };

        const response = await fetch("http://localhost:8000/news");
        const news: NewsArticle[] = await response.json();

        return (
          <main>
            <h1>NewsTalk AI</h1>
           {news.map((article) => (
            <NewsCard key = {article.id}
                      title = {article.title}
                      category = {article.category}
                      source = {article.source}/>
           ))}
          </main>
        );

}