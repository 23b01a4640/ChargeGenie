export default function AuthCard({ title, children, footer }) {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 px-4">
      <div className="w-full max-w-md bg-white rounded-2xl shadow-xl p-8">
        {/* Title */}
        <h2 className="text-2xl font-semibold text-gray-800 mb-6 text-center">
          {title}
        </h2>

        {/* Main Content (Login / Signup Form) */}
        <div>{children}</div>

        {/* Optional Footer (Signup / Login / Back links) */}
        {footer && (
          <div className="mt-6 pt-4 border-t text-center text-sm text-gray-600">
            {footer}
          </div>
        )}
      </div>
    </div>
  );
}
