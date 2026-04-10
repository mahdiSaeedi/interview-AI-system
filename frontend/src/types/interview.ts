export type QuestionItem = {
  id: string;
  prompt: string;
  intent?: string;
};

export type InterviewSession = {
  session_id: string;
  interview_title: string;
  questions: Array<{ id: string; prompt: string }>;
  answers: Array<{ question_id: string; response: string }>;
  current_question_index: number;
  is_complete: boolean;
};

export type AnalysisResult = {
  session_id: string;
  summary: string;
  themes: string[];
  recommendations: string[];
};
