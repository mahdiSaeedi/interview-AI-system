import { ReactNode } from "react";

type AppShellProps = {
  children: ReactNode;
};

export function AppShell({ children }: AppShellProps) {
  return (
    <main className="app-shell">
      <header className="hero">
        <p className="muted">Agent-driven interview workflow</p>
        <h1>Interview System</h1>
        <p className="muted">
          Generate questions, conduct interviews, and analyze answers in separate phases.
        </p>
      </header>
      <section className="panel-grid">{children}</section>
    </main>
  );
}
