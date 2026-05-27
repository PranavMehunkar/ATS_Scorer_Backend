<h1>AI Resume ATS System (Backend)</h1>
<h2>Overview</h2>
This is backend of AI-Powered ATS Resume Analyzer that evaluates resumes, matches them with job descriptions, and provides intelligent feedback for ATS optimization. This project strengthened skills in AI integration, backend development, cloud deployment, and scalable full-stack application development.

<h2>Table of Contents</h2>
<li>Overview</li>
<li>Tech Stack</li>
<li>Features</li>
<li>Installation</li>
<li>Usage</li>
<li>Deployment</li>
<li>License</li>
<h2>Tech Stack</h2>
<h3>Backend</h3>
<li>FastAPI</li>
<h3>Database</h3>
<li>Supabase</li>
<h3>Deployment</h3>
<li>Render</li>
<h3>Development Tools</h3>
<li>Visual Studio Code</li>
<li>Git</li>
<li>GitHub</li>
<h3>Features</h3>
<li>AI-powered resume parsing using NLP</li>
<li>ATS score calculation with detailed component breakdown</li>
<li>Job Description matching & missing keyword detection</li>
<li>Skill validation based on projects and experience</li>
<li>PDF report generation</li>
<li>Google Authentication with Supabase</li>
<li>Resume history tracking dashboard</li>
<h2>Installation</h2>
To run ATS_Scorer_Backend locally, follow these steps:

<h3>1. Clone the repository:</h3>

<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>git clone https://github.com/yourusername/ATS_Scorer_Backend.git</code></pre>
</div>

<h3>2. Navigate to the project directory:</h3>

<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>cd ATS_Scorer_Backend</code></pre>
</div>

<h3>3. Install the dependencies:</h3>

<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>pip install fastapi</code></pre>
</div>
<h3>4. Set up environment variables:</h3>

Create a .env file in the root directory and configure the following variables:

<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>SUPABASE_URL=&lt;your_supabase_url&gt;</code></pre>
</div>
<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>SUPABASE_KEY=&lt;your_supabase_key&gt;</code></pre>
</div>
<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>SUPABASE_ANON_KEY=&lt;your_supabase_anon_key&gt;</code></pre>
</div>
<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>GROQ_API_KEY=&lt;your_groq_api_key&gt;</code></pre>
</div>
<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>AUTH_REDIRECT_URL="http://localhost:8501/auth/v1/callback"</code></pre>
</div>v

<h3>5. Run the development server:</h3>

<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>uvicorn backend.main:app --reload</code></pre>
</div>
<h3>6. Open your browser and navigate to:</h3>

<div class="bg-light p-3 rounded border">
  <pre class="mb-0">
    <code>http://localhost:8000</code></pre>
</div>
<h2>Usage</h2>
Once the application is running, you can:

<h3><li>See Various Requests:</h3>See various requests with ATS Resume Analyzer title.</li>

<h2>Deployment</h2>
ATS_Scorer_Backend is deployed on Render. For deployment, ensure you have the Render CLI configured.
Ensure your Render credentials and services are properly set up for deployment.

<h2>License</h2>
All rights reserved.
