"use client";
import { useState } from "react";
type ErrorPageProps = {
  error: Error & { digest?: string };
  reset: () => void;
};
export default function ErrorPage({
  error,
  reset,
}: ErrorPageProps) {
  const [retrying, setRetrying] = useState(false);
function handleRetry() {
  window.location.reload();
}
  return (
    <main className="max-w-3xl mx-auto p-8 text-center">
      <h1 className="text-2xl font-bold mb-4">
        Unable to load NewsTalk AI
      </h1>

      <p className="text-gray-600 mb-6">
        We couldn't load the news right now.
        Please try again.
      </p>
        <button
        type="button"
        onClick={handleRetry}
        className="cursor-pointer rounded-lg bg-black px-6 py-3 text-white"
        >
        Try again
        </button>
    </main>
  );
}
