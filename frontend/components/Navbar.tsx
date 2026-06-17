import Link from "next/link"
export default function Navbar(){
    return(
        <nav className="flex justify-between items-center mb-8">
            <h1 className="text-2xl font-bold">
                NewsTalk AI
                </h1>
            <div className="flex gap-6">
                <Link href = "/">For You</Link>
                <Link href = "/trending">Trending</Link>
                <Link href = "/instant">Instant</Link>
                <Link href = "/profile">Profile</Link>
            </div>
        </nav>
    );
}