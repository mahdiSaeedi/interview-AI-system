import { AppShell } from "./components/AppShell";
import { AnalysisPage } from "./pages/AnalysisPage";
import { HomePage } from "./pages/HomePage";
import { InterviewPage } from "./pages/InterviewPage";

export function App() {
  return (
    <AppShell>
      <HomePage />
      <InterviewPage />
      <AnalysisPage />
    </AppShell>
  );
}
