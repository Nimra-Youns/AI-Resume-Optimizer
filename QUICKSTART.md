# Quick Start Guide - 10 Minutes

## Step 1: Install (2 minutes)

```bash
# Clone the repo
git clone https://github.com/yourusername/ai-resume-optimizer.git
cd ai-resume-optimizer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Get API Key (3 minutes)

1. Go to https://console.anthropic.com
2. Sign up (free account)
3. Create API key
4. Create `.env` file:
   ```
   ANTHROPIC_API_KEY=sk-ant-your-key-here
   ```

## Step 3: Test It (2 minutes)

```bash
# Generate a cover letter with sample files
python app.py \
  --resume samples/sample_resume.txt \
  --job samples/sample_job_description.txt \
  --action cover_letter \
  --output my_cover_letter.txt

# Check the output
cat my_cover_letter.txt
```

## Step 4: Use Your Documents (3 minutes)

1. Create `my_resume.txt` with your resume
2. Create `job_description.txt` with job posting
3. Run:
   ```bash
   python app.py \
     --resume my_resume.txt \
     --job job_description.txt \
     --action cover_letter \
     --output output.txt
   ```

---

## Available Actions

### 1. Cover Letter Generation
```bash
python app.py --resume your_resume.txt --job job.txt --action cover_letter
```
Creates a tailored cover letter matching job requirements

### 2. Resume Analysis
```bash
python app.py --resume your_resume.txt --action analyze
```
Get feedback on strengths, improvements, and ATS optimization

### 3. Market Trends
```bash
python app.py --job job.txt --action trends
```
Understand in-demand skills and industry insights

### 4. Keyword Extraction
```bash
python app.py --job job.txt --action keywords
```
Extract and categorize all keywords from job posting

### 5. Rewrite Summary
```bash
python app.py --resume your_resume.txt --job job.txt --action rewrite_summary
```
Get a professionally rewritten professional summary

### 6. ATS Optimization
```bash
python app.py --resume your_resume.txt --action ats_optimize
```
Optimize resume for Applicant Tracking Systems

### 7. Interview Prep
```bash
python app.py --resume your_resume.txt --job job.txt --action interview_prep
```
Get interview questions and preparation guide

---

## Example Workflow

### Day 1: Find a Job
- Paste job description into `target_job.txt`

### Day 2: Analyze
```bash
# What skills are they looking for?
python app.py --job target_job.txt --action keywords

# What's the market saying?
python app.py --job target_job.txt --action trends
```

### Day 3: Customize
```bash
# Rewrite my professional summary
python app.py --resume my_resume.txt --job target_job.txt --action rewrite_summary

# Generate cover letter
python app.py --resume my_resume.txt --job target_job.txt --action cover_letter
```

### Day 4: Prepare
```bash
# Prepare for interviews
python app.py --resume my_resume.txt --job target_job.txt --action interview_prep
```

### Day 5: Optimize
```bash
# Make sure ATS can read my resume
python app.py --resume my_resume.txt --action ats_optimize
```

---

## Tips for Best Results

1. **Detailed Resume**
   - Include specific achievements and metrics
   - Use action verbs
   - Include years of experience

2. **Complete Job Description**
   - Copy entire job posting (more context = better results)
   - Include company info if available
   - Include salary/benefits info if listed

3. **Review Output**
   - AI generates suggestions, not final answers
   - Always review and personalize
   - Trust your judgment on what feels authentic

4. **Iterate**
   - Run analysis multiple times
   - Try different formulations
   - Save your best outputs

---

## Cost & Free Trial

- **Anthropic offers free credits** when you create account
- Typical use: $0.10-0.50 per job application
- Monitor usage at: https://console.anthropic.com/usage

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "API key not found" | Check .env file in project root |
| "Module not found" | Run: `pip install -r requirements.txt` |
| "File not found" | Use correct path: `./my_resume.txt` or absolute path |
| Slow responses | First request is slowest, wait patiently |
| Rate limits | Spread requests over time, check usage |

---

## Next Steps

1. ✅ Test with samples
2. ✅ Add your actual resume
3. ✅ Find a target job
4. ✅ Run all actions
5. ✅ Customize the output
6. ✅ Submit your application!

---

## Want to Contribute?

- Fix a bug? Submit a PR
- Have an idea? Open an issue
- Want to add a feature? Fork and develop

---

## Support

- 📖 Full docs: See README.md
- 📚 Setup guide: See SETUP.md
- 🤔 API help: https://docs.claude.com
- 💬 GitHub Issues: Report problems

---

**Good luck with your job search! 🚀**

Built with Claude AI by Anthropic
