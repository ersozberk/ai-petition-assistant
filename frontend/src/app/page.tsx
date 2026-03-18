"use client";

import { useState } from "react";

export default function Home() {
  const [complaint, setComplaint] = useState("");
  const [company, setCompany] = useState("");
  const [petition, setPetition] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleGenerate = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setPetition("");

    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/generate-petition`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          user_complaint: complaint,
          company_name: company,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Bir hata oluştu.");
      }

      setPetition(data.petition_text);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-3xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-extrabold text-gray-900 mb-4">
            ⚖️ AI Dilekçe Asistanı
          </h1>
          <p className="text-lg text-gray-600">
            Tüketici haklarınızı korumak için yapay zeka destekli, güvenli dilekçe oluşturucu.
          </p>
        </div>

        <div className="bg-white shadow-xl rounded-2xl p-8 mb-8">
          <form onSubmit={handleGenerate} className="space-y-6">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Şikayet Edilen Firma
              </label>
              <input
                type="text"
                required
                className="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 outline-none transition"
                placeholder="Örn: X Kargo, Y Teknoloji A.Ş."
                value={company}
                onChange={(e) => setCompany(e.target.value)}
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Olay Özeti (Lütfen detaylı anlatın)
              </label>
              <textarea
                required
                rows={5}
                className="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 outline-none transition"
                placeholder="Yaşadığınız mağduriyeti, tarihleri ve kişisel bilgilerinizi (TC, Tel vb.) yazabilirsiniz. AI sistemimize bilgileriniz maskelenerek gönderilir."
                value={complaint}
                onChange={(e) => setComplaint(e.target.value)}
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className={`w-full py-4 rounded-lg font-bold text-white transition shadow-lg ${
                loading ? "bg-gray-400 cursor-not-allowed" : "bg-blue-600 hover:bg-blue-700"
              }`}
            >
              {loading ? "Dilekçe Hazırlanıyor..." : "Dilekçeyi Oluştur"}
            </button>
          </form>
        </div>

        {error && (
          <div className="bg-red-50 border-l-4 border-red-500 p-4 mb-8">
            <p className="text-red-700">{error}</p>
          </div>
        )}

        {petition && (
          <div className="bg-white shadow-xl rounded-2xl p-8 border border-green-100 animate-fade-in">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">Taslak Dilekçeniz</h2>
            <div className="bg-gray-50 p-6 rounded-lg border border-gray-200 whitespace-pre-wrap text-gray-800 leading-relaxed font-serif">
              {petition}
            </div>
            <button
              onClick={() => window.print()}
              className="mt-6 flex items-center justify-center gap-2 w-full sm:w-auto px-6 py-3 bg-green-600 text-white font-bold rounded-lg hover:bg-green-700 transition"
            >
              🖨️ Yazdır / PDF Kaydet
            </button>
          </div>
        )}
      </div>
    </main>
  );
}