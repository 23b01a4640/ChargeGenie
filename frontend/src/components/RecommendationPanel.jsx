export default function RecommendationPanel({ recommendation }) {
  if (!recommendation?.top_5?.length) return null;

  return (
    <div className="bg-white p-4 rounded-lg shadow mt-4">
      <h3 className="text-lg font-semibold mb-3">
        ⭐ Top Recommended Charging Stations
      </h3>

      <ul className="space-y-3">
        {recommendation.top_5.map((s, idx) => (
          <li key={s.place_id} className="border rounded p-3">
            <p className="font-medium">
              {idx + 1}. {s.name}
            </p>

            <p className="text-sm text-gray-600 mt-1">
              ⚡ {s.power_kw || "N/A"} kW &nbsp;|&nbsp;
              🔌 {s.connector} &nbsp;|&nbsp;
              🏢 {s.operator}
            </p>

            <p className="text-xs text-gray-500 mt-1">
              {recommendation.explanation}
            </p>
          </li>
        ))}
      </ul>
    </div>
  );
}
