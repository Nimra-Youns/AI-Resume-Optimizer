# Setup Guide - AI Resume & Cover Letter Optimizer

## Quick Start (5 minutes)

### 1. Prerequisites
- Python 3.10 or higher
- Git
- API key from Anthropic (free)

### 2. Clone Repository
```bash
git clone https://github.com/yourusername/ai-resume-optimizer.git
cd ai-resume-optimizer
```

### 3. Create Virtual Environment
```bash
# On Mac/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure API Key
```bash
# Copy example configuration
cp .env.example .env

# Edit .env and add your API key
# ANTHROPIC_API_KEY=sk-ant-your-actual-api-key
```

### 6. Test Installation
```bash
python app.py --help
```

---

## Getting Your Anthropic API Key

### Step-by-Step:

1. **Visit Anthropic Console**
   - Go to: https://console.anthropic.com
   - Sign up or log in with your account

2. **Navigate to API Keys**
   - Click on your profile icon (top right)
   - Select "API Keys"

3. **Create New Key**
   - Click "Create Key"
   - Give it a name (e.g., "Resume Optimizer")
   - Copy the generated key

4. **Add to .env File**
   ```
   ANTHROPIC_API_KEY=sk-ant-your-copied-key-here
   ```

5. **Save and Test**
   - Save the .env file
   - Run: `python app.py --help` to verify it works

---

## Usage Examples

### Example 1: Generate Tailored Cover Letter
```bash
python app.py \
  --resume samples/sample_resume.txt \
  --job samples/sample_job_description.txt \
  --action cover_letter \
  --output my_cover_letter.txt
```

### Example 2: Analyze Resume
```bash
python app.py \
  --resume samples/sample_resume.txt \
  --action analyze \
  --output resume_analysis.txt
```

### Example 3: Get Market Trends
```bash
python app.py \
  --job samples/sample_job_description.txt \
  --action trends \
  --output market_trends.txt
```

### Example 4: Optimize for ATS
```bash
python app.py \
  --resume samples/sample_resume.txt \
  --action ats_optimize \
  --output ats_optimized_resume.txt
```

### Example 5: Interview Preparation
```bash
python app.py \
  --resume samples/sample_resume.txt \
  --job samples/sample_job_description.txt \
  --action interview_prep \
  --output interview_guide.txt
```

### Example 6: Extract Keywords
```bash
python app.py \
  --job samples/sample_job_description.txt \
  --action keywords \
  --output keywords.json
```

---

## Using in Python Code

```python
from app import ResumeOptimizer

# Initialize
optimizer = ResumeOptimizer()

# Load documents
resume = optimizer.load_resume("path/to/resume.txt")
job = optimizer.load_job_description("path/to/job.txt")

# Get cover letter
cover_letter = optimizer.get_tailored_cover_letter(resume, job)

# Save result
optimizer.save_to_file(cover_letter, "my_cover_letter.txt")

# Get different analyses
market_analysis = optimizer.analyze_market_trends(job)
interview_prep = optimizer.get_interview_prep(resume, job)
ats_optimization = optimizer.optimize_for_ats(resume)

# Reset for new conversation
optimizer.reset_conversation()
```

---

## Troubleshooting

### Error: "API key not found"
**Solution:** 
- Check .env file has correct format: `ANTHROPIC_API_KEY=sk-ant-...`
- Make sure .env file is in project root directory
- Restart terminal/IDE after adding .env

### Error: "Module not found: anthropic"
**Solution:**
```bash
pip install anthropic==0.34.0
```

### Error: "File not found"
**Solution:**
- Use absolute paths or correct relative paths
- Check file names match exactly (case-sensitive on Mac/Linux)
- Example: `python app.py --resume ./samples/sample_resume.txt`

### Error: "Invalid API key"
**Solution:**
- Verify key starts with `sk-ant-`
- Generate a new key from https://console.anthropic.com
- Check for extra spaces or characters

### Slow responses
**Solution:**
- Normal for first request (API initialization)
- Subsequent requests should be faster
- Reduce MAX_TOKENS if needed in config

---

## File Organization Tips

### Recommended Structure
```
ai-resume-optimizer/
├── my_resume.txt              # Your actual resume
├── my_cover_letter.txt        # Generated cover letter
├── .env                       # Your API key (never commit!)
├── app.py
├── requirements.txt
├── samples/
│   ├── sample_resume.txt
│   └── sample_job_description.txt
└── output/                    # Generated files
    ├── cover_letter_v1.txt
    ├── interview_prep.txt
    └── ats_optimized.txt
```

### Adding Your Documents
1. Create `.txt` files with your content
2. Place them in project root or subfolder
3. Reference path in command: `--resume my_resume.txt`

---

## Advanced Configuration

### Edit config.example.py
```python
# Copy and customize
cp config.example.py config.py

# Edit settings:
API_KEY = "your-key"
MODEL = "claude-opus-4-6"
MAX_TOKENS = 2000
TEMPERATURE = 0.7
```

### Choose Different Models
```python
# Fast & efficient
MODEL = "claude-haiku-4.5"

# Balanced
MODEL = "claude-sonnet-4-6"

# Most capable (recommended)
MODEL = "claude-opus-4-6"
```

---

## API Usage & Costs

### Pricing Structure
- Varies by model and token usage
- Most cover letters: $0.05-0.20
- Market analysis: $0.10-0.30
- Interview prep: $0.20-0.50

### Monitoring Usage
- Check your usage at: https://console.anthropic.com/usage
- Monitor tokens in API responses
- Set alerts for budget limits

### Cost Optimization
- Use `claude-haiku-4.5` for simpler tasks
- Batch similar requests
- Cache repeated analyses

---

## Security Best Practices

### Do's ✓
- Keep .env file in .gitignore
- Use environment variables for API key
- Store documents locally only
- Review AI output before sharing

### Don'ts ✗
- Don't commit .env file to GitHub
- Don't share API key in emails or chat
- Don't use production API key in tutorials
- Don't trust AI output without review

### Protecting Sensitive Data
```python
# Never do this:
api_key = "sk-ant-xxxxx"  # Hard-coded

# Always do this:
api_key = os.getenv("ANTHROPIC_API_KEY")  # Environment variable
```

---

## Next Steps

1. **Start with samples**
   - Test with sample_resume.txt and sample_job_description.txt

2. **Add your documents**
   - Replace samples with your actual resume and target job

3. **Explore features**
   - Try different --action options
   - Refine outputs based on results

4. **Customize prompts**
   - Edit prompt strings in app.py for your needs
   - Test variations

5. **Integrate with workflow**
   - Build batch processing script
   - Integrate with job application workflow

---

## Support & Resources

### Documentation
- [Anthropic Claude API Docs](https://docs.claude.com)
- [Project README](../README.md)
- Example outputs in `/samples`

### Getting Help
- Check troubleshooting section above
- Review Claude API documentation
- Check GitHub Issues for similar problems

### Providing Feedback
- Found a bug? Open an issue on GitHub
- Have suggestions? Create a discussion
- Want to contribute? Submit a pull request

---

## System Requirements

### Minimum
- Python 3.10+
- 100MB disk space
- Internet connection for API

### Recommended
- Python 3.11+
- 500MB disk space
- High-speed internet
- 4GB+ RAM

### Tested On
- macOS 12+
- Windows 10+
- Ubuntu 20.04+
- WSL2 on Windows

---

**Ready to optimize your resume? Start with Example 1 above!**

Last Updated: May 2026
