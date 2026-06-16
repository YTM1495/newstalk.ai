export default function Navbar(){
    return(
        <nav className="flex justify-between items-center mb-8">
            <h1 className="text-2xl font-bold">
                NewsTalk AI
                </h1>
            <div className="flex gap-6">
                <span>For You</span>
                <span>Trending</span>
                <span>Instant</span>
                <span>Profile</span>
            </div>
        </nav>
    );
}