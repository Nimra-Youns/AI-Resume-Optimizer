"""
AI Resume & Cover Letter Optimizer
Uses Claude AI to analyze, tailor, and enhance resumes and cover letters
"""

import os
import json
from pathlib import Path
from typing import Optional
import argparse
from anthropic import Anthropic

class ResumeOptimizer:
    """Main application class for resume and cover letter optimization."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the optimizer with Anthropic API key."""
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key not found. Set ANTHROPIC_API_KEY environment variable "
                "or pass api_key parameter."
            )
        
        self.client = Anthropic(api_key=self.api_key)
        self.model = "claude-opus-4-6"
        self.conversation_history = []
    
    def load_document(self, file_path: str) -> str:
        """Load a text document from file."""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Document not found: {file_path}")
        
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def load_resume(self, file_path: str) -> str:
        """Load resume from file."""
        return self.load_document(file_path)
    
    def load_job_description(self, file_path: str) -> str:
        """Load job description from file."""
        return self.load_document(file_path)
    
    def _call_claude(self, user_message: str) -> str:
        """Call Claude API with conversation history."""
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            messages=self.conversation_history
        )
        
        assistant_message = response.content[0].text
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    def analyze_resume(self, resume: str) -> str:
        """Analyze resume and provide structured feedback."""
        prompt = f"""
        Please analyze this resume and provide detailed feedback on:
        1. Key strengths and accomplishments
        2. Skills highlighted
        3. Areas for improvement
        4. Formatting and readability
        5. ATS (Applicant Tracking System) optimization tips
        
        Resume:
        {resume}
        
        Provide actionable, specific suggestions.
        """
        
        return self._call_claude(prompt)
    
    def get_tailored_cover_letter(self, resume: str, job_description: str) -> str:
        """Generate a tailored cover letter based on resume and job description."""
        prompt = f"""
        Based on the following resume and job description, write a compelling, 
        personalized cover letter. The cover letter should:
        
        1. Address specific requirements from the job posting
        2. Highlight relevant experience from the resume
        3. Show enthusiasm for the role and company
        4. Include specific examples and achievements
        5. Be professional yet personable (3-4 paragraphs)
        
        Resume:
        {resume}
        
        Job Description:
        {job_description}
        
        Generate a cover letter that stands out while remaining professional.
        """
        
        return self._call_claude(prompt)
    
    def analyze_market_trends(self, job_description: str) -> str:
        """Analyze market trends based on job description."""
        prompt = f"""
        Based on this job description, provide market trend analysis including:
        
        1. In-demand skills for this role
        2. Current salary ranges (if discernible)
        3. Key qualifications trending in this field
        4. Industry growth areas
        5. Recommendations for skill development
        6. Related career paths
        
        Job Description:
        {job_description}
        
        Provide insights that would help a candidate position themselves better.
        """
        
        return self._call_claude(prompt)
    
    def extract_keywords(self, job_description: str) -> dict:
        """Extract keywords from job description."""
        prompt = f"""
        Extract and categorize keywords from this job description:
        
        Job Description:
        {job_description}
        
        Provide response as JSON with these categories:
        - skills: List of required technical and soft skills
        - qualifications: Required education and certifications
        - tools: Specific tools and technologies mentioned
        - keywords: Important industry terms and phrases
        - responsibilities: Key responsibilities mentioned
        
        Return ONLY valid JSON, no additional text.
        """
        
        response = self._call_claude(prompt)
        try:
            # Try to parse JSON from response
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            if json_start >= 0 and json_end > json_start:
                return json.loads(response[json_start:json_end])
        except json.JSONDecodeError:
            pass
        
        return {"raw_keywords": response}
    
    def rewrite_professional_summary(self, resume: str, job_description: str) -> str:
        """Rewrite professional summary to match job requirements."""
        prompt = f"""
        Rewrite the professional summary/objective section of this resume to:
        
        1. Align with the job description requirements
        2. Highlight relevant skills and experience
        3. Be compelling and concise (2-3 sentences)
        4. Include keywords from the job posting
        5. Use strong action verbs
        
        Current Resume:
        {resume}
        
        Target Job Description:
        {job_description}
        
        Provide the rewritten professional summary ready to use.
        """
        
        return self._call_claude(prompt)
    
    def optimize_for_ats(self, resume: str) -> str:
        """Optimize resume for ATS (Applicant Tracking Systems)."""
        prompt = f"""
        Analyze and optimize this resume for ATS (Applicant Tracking Systems).
        Provide:
        
        1. Current ATS compatibility issues
        2. Formatting recommendations
        3. Keyword optimization suggestions
        4. Specific improvements needed
        5. Optimized version of key sections
        
        Resume:
        {resume}
        
        Focus on practical, implementable changes.
        """
        
        return self._call_claude(prompt)
    
    def get_interview_prep(self, resume: str, job_description: str) -> str:
        """Generate interview preparation guide."""
        prompt = f"""
        Create an interview preparation guide based on this resume and job description.
        Include:
        
        1. Likely interview questions
        2. How to present relevant experience
        3. Questions to ask the interviewer
        4. Key points to emphasize
        5. Potential objections and responses
        6. STAR method examples from resume
        
        Resume:
        {resume}
        
        Job Description:
        {job_description}
        
        Make it practical and actionable.
        """
        
        return self._call_claude(prompt)
    
    def save_to_file(self, content: str, output_path: str) -> None:
        """Save content to file."""
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Saved to: {output_path}")
    
    def reset_conversation(self) -> None:
        """Reset conversation history for new context."""
        self.conversation_history = []


def main():
    """Command line interface."""
    parser = argparse.ArgumentParser(
        description="AI Resume & Cover Letter Optimizer"
    )
    parser.add_argument(
        "--resume", 
        help="Path to resume file"
    )
    parser.add_argument(
        "--job", 
        help="Path to job description file"
    )
    parser.add_argument(
        "--output", 
        default="output.txt",
        help="Output file path"
    )
    parser.add_argument(
        "--action",
        choices=[
            "analyze", 
            "cover_letter", 
            "trends", 
            "keywords", 
            "rewrite_summary", 
            "ats_optimize",
            "interview_prep"
        ],
        default="cover_letter",
        help="Action to perform"
    )
    
    args = parser.parse_args()
    
    # Initialize optimizer
    try:
        optimizer = ResumeOptimizer()
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    # Load documents
    resume = None
    job_description = None
    
    if args.resume:
        resume = optimizer.load_resume(args.resume)
        print(f"✓ Loaded resume from: {args.resume}")
    
    if args.job:
        job_description = optimizer.load_job_description(args.job)
        print(f"✓ Loaded job description from: {args.job}")
    
    # Perform requested action
    result = None
    
    try:
        if args.action == "analyze" and resume:
            print("\nAnalyzing resume...")
            result = optimizer.analyze_resume(resume)
        
        elif args.action == "cover_letter" and resume and job_description:
            print("\nGenerating tailored cover letter...")
            result = optimizer.get_tailored_cover_letter(resume, job_description)
        
        elif args.action == "trends" and job_description:
            print("\nAnalyzing market trends...")
            result = optimizer.analyze_market_trends(job_description)
        
        elif args.action == "keywords" and job_description:
            print("\nExtracting keywords...")
            keywords = optimizer.extract_keywords(job_description)
            result = json.dumps(keywords, indent=2)
        
        elif args.action == "rewrite_summary" and resume and job_description:
            print("\nRewriting professional summary...")
            result = optimizer.rewrite_professional_summary(resume, job_description)
        
        elif args.action == "ats_optimize" and resume:
            print("\nOptimizing for ATS...")
            result = optimizer.optimize_for_ats(resume)
        
        elif args.action == "interview_prep" and resume and job_description:
            print("\nGenerating interview preparation guide...")
            result = optimizer.get_interview_prep(resume, job_description)
        
        else:
            print("Error: Missing required files for this action")
            return
        
        # Save and display result
        if result:
            print("\n" + "="*60)
            print("RESULT:")
            print("="*60)
            print(result)
            print("="*60)
            
            optimizer.save_to_file(result, args.output)
    
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
