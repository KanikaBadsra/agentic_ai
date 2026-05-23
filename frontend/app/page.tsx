"use client";

import { useState } from "react";

import axios from "axios";


export default function Home() {

  const [question, setQuestion] = useState("");

  const [loading, setLoading] = useState(false);

  const [response, setResponse] = useState<any>(null);


  const askQuestion = async () => {

    if (!question) return;

    setLoading(true);

    try {

      const res = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          question,
          session_id: "demo_user"
        }
      );

      setResponse(res.data);

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);
    }
  };


  return (

    <main className="min-h-screen p-10 bg-gray-100">

      <div className="max-w-4xl mx-auto bg-white p-8 rounded-2xl shadow-lg">

        <h1 className="text-4xl font-bold mb-6">

          NexusIQ Dashboard
        </h1>


        <textarea
          className="w-full border p-4 rounded-lg"
          rows={4}
          placeholder="Ask business question..."
          value={question}
          onChange={(e) =>
            setQuestion(e.target.value)
          }
        />


        <button
          onClick={askQuestion}
          className="mt-4 bg-black text-white px-6 py-3 rounded-lg"
        >
          {loading ? "Thinking..." : "Ask"}
        </button>


        {response && (

          <div className="mt-8 space-y-6">

            <div>
              <h2 className="text-2xl font-semibold">
                Route
              </h2>

              <p>{response.route}</p>
            </div>


            <div>
              <h2 className="text-2xl font-semibold">
                SQL Query
              </h2>

              <pre className="bg-gray-200 p-4 rounded-lg overflow-auto">
                {response.sql_query}
              </pre>
            </div>


            <div>
              <h2 className="text-2xl font-semibold">
                Final Answer
              </h2>

              <p>{response.final_answer}</p>
            </div>


            <div>
              <h2 className="text-2xl font-semibold">
                Report Path
              </h2>

              <p>{response.report_path}</p>
            </div>

          </div>
        )}

      </div>

    </main>
  );
}