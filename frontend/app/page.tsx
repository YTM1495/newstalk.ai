export default async function Home(){
        type NewsArticle = {
          id:number;
          title:string;
          category:string;
        };

        const response = await fetch("http://localhost:8000/news");
        const news: NewsArticle[] = await response.json();

        return (
          <main>
            <h1>NewsTalk AI</h1>
           {news.map((article) => (
              <div key = {article.id}>
                <h2>{article.title}</h2>
                <p>{article.category}</p>
              </div>
           ))}
          </main>
        );

}