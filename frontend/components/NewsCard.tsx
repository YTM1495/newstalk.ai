type NewsCardProps = {
    title:string;
    category:string;
    source:string;
    date:string;
};

export default function NewsCard({
    title,category,source,date
} : NewsCardProps){
    return (
        <div className ="border rounded-lg p-4 mb-4 shadow-sm">
            <h2 className ="text-xl font-semibold">
                {title}
                </h2>
            <p className = "text-gray-600">
                {category}
                </p>
                <p className = "text-gray-600">{source}</p>
                <p className="text-gray-600">{date}</p>
        </div>
    );
}