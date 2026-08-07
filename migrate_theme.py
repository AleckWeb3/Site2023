#!/usr/bin/env python3
"""Migrate old-theme pages to the new dark theme from index.html."""
import re

# Read the dark theme reference
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract the <style> block from index.html
style_match = re.search(r'<style>(.*?)</style>', index_html, re.DOTALL)
dark_style = style_match.group(1)

# Extract the nav HTML from index.html (the <nav>...</nav> block)
nav_match = re.search(r'<nav>(.*?)</nav>', index_html, re.DOTALL)
dark_nav = nav_match.group(1)

# Extract the footer HTML from index.html
footer_match = re.search(r'<footer>(.*?)</footer>', index_html, re.DOTALL)
dark_footer = footer_match.group(1)

# Extract starfield JS from index.html
js_match = re.search(r'<script>(.*?)</script>', index_html, re.DOTALL)
dark_js = js_match.group(1)

# Extract SEO head additions (canonical, og, twitter, favicon) from index.html
# Get everything between </title> and <style>
head_match = re.search(r'</title>\n(.*?)<style>', index_html, re.DOTALL)
seo_head = head_match.group(1).strip()

def build_dark_page(title, meta_desc, body_content, extra_css=''):
    """Wrap content in the new dark theme shell."""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_desc}">
    <title>{title}</title>
    <link rel="canonical" href="https://webthreeinnovations.com/">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://webthreeinnovations.com/">
    <meta property="og:image" content="https://webthreeinnovations.com/Web-Three-Innovations-logo-dark-background.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{meta_desc}">
    <link rel="icon" type="image/png" href="Web-Three-Innovations-logo-dark-background.png">
    <style>
        * {{ margin:0; padding:0; box-sizing:border-box; }}
        :root {{
            --bg: #050508;
            --surface: #0e0e14;
            --surface-hover: #16161f;
            --border: #1a1a26;
            --border-hover: #2a2a3a;
            --text: #c8c8d4;
            --text-dim: #6b6b7a;
            --text-bright: #e8e8f0;
        }}
        body {{ font-family:'Segoe UI',system-ui,-apple-system,sans-serif; background:var(--bg); color:var(--text); overflow-x:hidden; line-height:1.6; -webkit-font-smoothing:antialiased; }}
        #stars-canvas {{ position:fixed; top:0; left:0; width:100%; height:100%; z-index:0; }}
        .content {{ position:relative; z-index:1; }}
        header {{ padding:1.2rem 5%; background:rgba(5,5,8,0.85); backdrop-filter:blur(16px); -webkit-backdrop-filter:blur(16px); position:sticky; top:0; z-index:100; border-bottom:1px solid rgba(255,255,255,0.06); }}
        nav {{ display:flex; justify-content:space-between; align-items:center; max-width:1400px; margin:0 auto; }}
        .logo a {{ display:flex; align-items:center; text-decoration:none; gap:0.6rem; }}
        .logo img {{ height:60px; width:auto; flex-shrink:0; }}
        @media(max-width:1024px){{ .logo img {{ height:48px; }} }}
        @media(max-width:768px){{ .logo img {{ height:36px; }} .nav-links {{ display:none; }} }}
        .logo-text {{ font-size:1.3rem; font-weight:300; color:var(--text-bright); letter-spacing:0.15em; }}
        .logo-sub {{ font-size:0.55rem; color:var(--text-dim); text-transform:uppercase; letter-spacing:0.2em; }}
        .nav-links {{ display:flex; gap:2.5rem; list-style:none; align-items:center; }}
        .nav-links a,.dropdown-toggle {{ color:var(--text-dim); text-decoration:none; font-weight:500; font-size:0.9rem; letter-spacing:0.02em; transition:color 0.3s; text-transform:uppercase; cursor:pointer; }}
        .nav-links a:hover,.dropdown-toggle:hover {{ color:var(--text-bright); }}
        .dropdown {{ position:relative; }}
        .dropdown-arrow {{ font-size:0.6rem; transition:transform 0.3s; opacity:0.5; }}
        .dropdown:hover .dropdown-arrow {{ transform:rotate(180deg); opacity:1; }}
        .dropdown-menu {{ position:absolute; top:100%; left:50%; transform:translateX(-50%) translateY(12px); background:rgba(14,14,20,0.97); backdrop-filter:blur(20px); border:1px solid var(--border); border-radius:8px; padding:0.4rem 0; min-width:220px; opacity:0; visibility:hidden; transition:all 0.25s; list-style:none; z-index:101; }}
        .dropdown:hover .dropdown-menu {{ opacity:1; visibility:visible; transform:translateX(-50%) translateY(6px); }}
        .dropdown-menu li {{ padding:0; }}
        .dropdown-menu a {{ display:block; padding:0.65rem 1.4rem; color:var(--text-dim); text-decoration:none; font-weight:400; font-size:0.85rem; transition:all 0.2s; white-space:nowrap; text-transform:none; letter-spacing:0; }}
        .dropdown-menu a:hover {{ background:rgba(255,255,255,0.04); color:var(--text-bright); }}
        .btn {{ padding:0.7rem 1.8rem; background:var(--surface); color:var(--text-bright); border:1px solid var(--border); border-radius:6px; font-weight:500; font-size:0.85rem; letter-spacing:0.03em; cursor:pointer; transition:all 0.3s; text-decoration:none; display:inline-block; text-transform:uppercase; }}
        .btn:hover {{ border-color:var(--border-hover); background:var(--surface-hover); box-shadow:0 0 30px rgba(255,255,255,0.03); }}
        .page-hero {{ min-height:30vh; display:flex; align-items:center; justify-content:center; text-align:center; padding:3rem 5%; position:relative; }}
        .page-hero h1 {{ font-size:2.8rem; color:var(--text-bright); font-weight:300; letter-spacing:-0.02em; }}
        .page-hero p {{ font-size:1.1rem; color:var(--text-dim); max-width:650px; margin:0.5rem auto 0; }}
        .section {{ padding:3rem 5%; max-width:900px; margin:0 auto; }}
        .section h2 {{ font-size:1.8rem; color:var(--text-bright); font-weight:300; margin-bottom:1rem; }}
        .section h3 {{ font-size:1.2rem; color:var(--text-bright); margin:1.5rem 0 0.5rem; font-weight:500; }}
        .section p {{ color:var(--text-dim); line-height:1.8; font-size:1.05rem; margin-bottom:1.5rem; }}
        .section ul {{ padding-left:1.5rem; }}
        .section li {{ color:var(--text-dim); line-height:1.8; font-size:1.05rem; margin-bottom:0.5rem; }}
        .policy-card {{ background:var(--surface); border:1px solid var(--border); border-radius:10px; padding:2rem; margin-bottom:1rem; }}
        .policy-card h4 {{ color:var(--text-bright); font-weight:500; font-size:1rem; margin-bottom:0.5rem; }}
        .policy-card p {{ color:var(--text-dim); font-size:0.95rem; line-height:1.7; }}
        .cta-section {{ padding:5rem 5%; text-align:center; position:relative; }}
        .cta-section::before {{ content:''; position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:400px; height:400px; background:radial-gradient(circle,rgba(255,255,255,0.015) 0%,transparent 70%); pointer-events:none; }}
        .cta-section h2 {{ font-size:2rem; margin-bottom:1rem; color:var(--text-bright); font-weight:300; }}
        .cta-section p {{ font-size:1rem; margin-bottom:2rem; color:var(--text-dim); }}
        .form-section {{ padding:2rem 5% 5rem; max-width:650px; margin:0 auto; }}
        .form-group {{ margin-bottom:1.5rem; }}
        .form-group label {{ display:block; margin-bottom:0.5rem; color:var(--text-dim); font-weight:500; font-size:0.9rem; }}
        .form-group input,.form-group textarea,.form-group select {{ width:100%; padding:0.8rem; background:var(--surface); border:1px solid var(--border); border-radius:8px; color:var(--text-bright); font-size:1rem; font-family:inherit; }}
        .form-group textarea {{ min-height:120px; resize:vertical; }}
        .form-group input:focus,.form-group textarea:focus,.form-group select:focus {{ outline:none; border-color:var(--border-hover); }}
        .form-note {{ color:var(--text-dim); font-size:0.85rem; margin-top:0.5rem; opacity:0.7; }}
        .flow-track {{ display:flex; gap:.75rem; overflow-x:auto; padding:1rem 0; }}
        .flow-step {{ flex:0 0 280px; background:var(--surface); border:1px solid var(--border); border-radius:10px; padding:1.8rem; transition:all .3s; }}
        .flow-step:hover {{ border-color:var(--border-hover); background:var(--surface-hover); }}
        .flow-step .step-num {{ font-size:.65rem; color:var(--text-dim); text-transform:uppercase; letter-spacing:.12em; margin-bottom:.8rem; }}
        .flow-step h4 {{ color:var(--text-bright); font-weight:500; font-size:1rem; margin-bottom:.5rem; }}
        .flow-step p {{ color:var(--text-dim); font-size:.85rem; line-height:1.65; margin:0; }}
        .flow-connector {{ display:flex; align-items:center; justify-content:center; flex:0 0 30px; color:var(--text-dim); font-size:1.5rem; opacity:0.3; }}
        .integration-grid {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(250px,1fr)); gap:1.5rem; }}
        .integration-card {{ background:var(--surface); border:1px solid var(--border); border-radius:10px; padding:1.5rem; }}
        .integration-card:hover {{ border-color:var(--border-hover); }}
        .integration-card h4 {{ color:var(--text-bright); margin-bottom:0.5rem; font-weight:500; }}
        .integration-card p {{ color:var(--text-dim); font-size:0.9rem; margin:0; }}
        {extra_css}
        footer {{ padding:3rem 5%; background:var(--surface); border-top:1px solid var(--border); }}
        .footer-grid {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(180px,1fr)); gap:2rem; max-width:1200px; margin:0 auto 2rem; }}
        .footer-col h4 {{ color:var(--text-dim); margin-bottom:1rem; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; }}
        .footer-col a {{ display:block; color:rgba(255,255,255,0.3); text-decoration:none; padding:0.25rem 0; font-size:0.85rem; transition:color 0.3s; }}
        .footer-col a:hover {{ color:var(--text-bright); }}
        .footer-bottom {{ text-align:center; color:rgba(255,255,255,0.15); font-size:0.75rem; max-width:1200px; margin:0 auto; letter-spacing:0.04em; }}
        @media(max-width:768px){{ .page-hero h1 {{ font-size:2rem; }} }}
    </style>
</head>
<body>
    <canvas id="stars-canvas"></canvas>
    <div class="content">
        <header>
            <nav>
                <div class="logo">
                    <a href="index.html">
                        <img src="Web-Three-Innovations-logo-dark-background.png" alt="Web Three Innovations">
                        <div><span class="logo-text">W3I</span><br><span class="logo-sub">Web Three Innovations</span></div>
                    </a>
                </div>
                <ul class="nav-links">
                    <li class="dropdown">
                        <span class="dropdown-toggle">Products <span class="dropdown-arrow">&#9662;</span></span>
                        <ul class="dropdown-menu">
                            <li><a href="apex-ai.html">Apex AI</a></li>
                            <li><a href="exagent.html">Exagent</a></li>
                            <li><a href="agent-consensus.html">Agent Consensus</a></li>
                        </ul>
                    </li>
                    <li><a href="index.html#about">Approach</a></li>
                    <li><a href="index.html#faq">FAQ</a></li>
                    <li><a href="ai-agent-interface.html" style="font-size:0.75rem;opacity:0.5;letter-spacing:0.1em;">AI Agent Interface</a></li>
                </ul>
                <a href="contact.html" class="btn">Contact</a>
            </nav>
        </header>
{body_content}
        <footer>
            <div class="footer-grid">
                <div class="footer-col"><h4>Products</h4><a href="apex-ai.html">Apex AI</a><a href="exagent.html">Exagent</a><a href="agent-consensus.html">Agent Consensus</a></div>
                <div class="footer-col"><h4>Company</h4><a href="about.html">About</a><a href="contact.html">Contact</a></div>
                <div class="footer-col"><h4>Resources</h4><a href="security.html">Security</a><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Service</a></div>
            </div>
            <div class="footer-bottom"><p>&copy; 2026 Web Three Innovations. All Rights Reserved.</p></div>
        </footer>
    </div>
    <script>
        const c=document.getElementById('stars-canvas'),ctx=c.getContext('2d');c.width=window.innerWidth;c.height=window.innerHeight;
        let S=[];for(let i=0;i<200;i++)S.push({{x:Math.random()*c.width,y:Math.random()*c.height,r:Math.random()*0.8+0.2,o:Math.random()*0.4+0.1,s:Math.random()*0.15+0.03}});
        function A(){{ctx.fillStyle='rgba(5,5,8,0.15)';ctx.fillRect(0,0,c.width,c.height);S.forEach(s=>{{s.y+=s.s;if(s.y>c.height){{s.y=0;s.x=Math.random()*c.width}}ctx.beginPath();ctx.arc(s.x,s.y,s.r,0,Math.PI*2);ctx.fillStyle=`rgba(180,190,210,${{s.o}})`;ctx.fill()}});requestAnimationFrame(A)}}A();
        window.addEventListener('resize',()=>{{c.width=window.innerWidth;c.height=window.innerHeight}});
        document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',function(e){{e.preventDefault();let t=document.querySelector(this.getAttribute('href'));if(t)t.scrollIntoView({{behavior:'smooth',block:'start'}})}}));
    </script>
</body>
</html>'''

# ====== ABOUT PAGE ======
about_body = '''
        <section class="page-hero"><div><h1>About Web Three Innovations</h1><p>Building practical AI tools for enterprise operations.</p></div></section>
        <section class="section">
            <h2>Who We Are</h2>
            <p>Web Three Innovations is a software company focused on building practical tools that solve real operational problems. We believe AI should make work easier — not replace human judgment.</p>
            <p>Our first product, Apex AI, automates top-of-funnel sales development — researching target companies, qualifying them against your rules, preparing approved outreach, handling replies, and delivering qualified leads. We build with transparency: the AI flags and suggests; humans decide and audit.</p>
            <p>We're a small, experienced team with backgrounds in enterprise software, AI integration, and operations consulting. We prioritize reliability, security, and honest communication over hype.</p>
        </section>
        <section class="section">
            <h2>Our Approach</h2>
            <p>Enterprise-minded from day one. AI doesn't slot neatly into existing IT SOPs — we know that. Our approach keeps your IT team happy by running in isolated environments that never compromise your enterprise data or integrity.</p>
            <p>We ship early and iterate based on real feedback. Every feature we build starts with a clear problem statement and measurable outcome. We don't add AI where a simpler solution works better.</p>
            <p>We're transparent about what our software can and cannot do. We share limitations openly and never claim our AI is infallible.</p>
        </section>
'''

# ====== CONTACT PAGE ======
contact_body = '''
        <section class="page-hero"><div><h1>Request Early Access</h1><p>Tell us about your use case and we'll point you to the right product.</p></div></section>
        <section class="form-section">
            <form name="early-access" method="POST" data-netlify="true" action="/thank-you">
                <input type="hidden" name="form-name" value="early-access">
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Work Email</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="role">Your Role</label>
                    <select id="role" name="role">
                        <option value="">Select...</option>
                        <option value="operations">Operations</option>
                        <option value="sales">Sales / Business Development</option>
                        <option value="executive">Executive / Owner</option>
                        <option value="it">IT / Security</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="product">Which product are you interested in?</label>
                    <select id="product" name="product">
                        <option value="">Select...</option>
                        <option value="apex-ai">Apex AI (Sales Automation)</option>
                        <option value="exagent">Exagent (AI Trading)</option>
                        <option value="agent-consensus">Agent Consensus (DevOps Integration)</option>
                        <option value="not-sure">Not sure — show me what fits</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="scope">Describe your use case or current workflow</label>
                    <input type="text" id="scope" name="scope" placeholder="e.g., top-of-funnel outreach to 300 target accounts, or exploring LLM trading...">
                </div>
                <div class="form-group">
                    <label for="message">Anything else we should know?</label>
                    <textarea id="message" name="message"></textarea>
                </div>
                <p class="form-note">We'll respond within 2 business days. No spam, no sharing your data.</p>
                <button type="submit" class="btn" style="width:100%; margin-top:1rem; font-size:1.1rem;">Submit Request</button>
            </form>
            <p style="text-align:center; margin-top:2rem; color:var(--text-dim); font-size:0.9rem;">Or email us directly: <a href="mailto:info@webthreeinnovations.com" style="color:var(--text-bright);">info@webthreeinnovations.com</a></p>
        </section>
'''

# ====== HOW IT WORKS PAGE ======
how_it_works_body = '''
        <section class="page-hero"><div><h1>How Apex AI Works</h1><p>Eight stages from target company to qualified lead handoff — one continuous, controlled workflow.</p></div></section>
        <section class="section">
            <h2>The Sales Development Workflow</h2>
            <div class="flow-track">
                <div class="flow-step"><div class="step-num">01 Setup</div><h4>Sales Plan Configuration</h4><p>Define your company and offer, target rules, buyer roles, message guidance, follow-up plans, email connection, sending limits, and lead handoff — once per campaign.</p></div>
                <div class="flow-connector">→</div>
                <div class="flow-step"><div class="step-num">02 Input</div><h4>Add Target Companies</h4><p>Add one company, upload a list, or let Apex find targets under your active sales plan.</p></div>
                <div class="flow-connector">→</div>
                <div class="flow-step"><div class="step-num">03 Research</div><h4>Company Fit Analysis</h4><p>Research each company, record sources, and apply your Company Fit rules with deterministic scoring.</p></div>
                <div class="flow-connector">→</div>
                <div class="flow-step"><div class="step-num">04 Contact</div><h4>Contact Discovery</h4><p>Find one current contact in an approved role with valid email. If unverifiable, try another role or defer.</p></div>
                <div class="flow-connector">→</div>
                <div class="flow-step"><div class="step-num">05 Message</div><h4>Outreach Preparation</h4><p>Prepare messages under your sales plan. Edit any message or request a new version. Only exceptions need your review.</p></div>
                <div class="flow-connector">→</div>
                <div class="flow-step"><div class="step-num">06 Launch</div><h4>Approve & Start</h4><p>One approval activates the complete plan. Runs through email with sending controls.</p></div>
                <div class="flow-connector">→</div>
                <div class="flow-step"><div class="step-num">07 Reply</div><h4>Handle Replies</h4><p>Classify replies, handle opt-outs, stop follow-up after a response. Never chase someone who already engaged.</p></div>
                <div class="flow-connector">→</div>
                <div class="flow-step"><div class="step-num">08 Deliver</div><h4>Qualified Lead Handoff</h4><p>Download CSV or JSON and import into your sales system. Your reps receive qualified leads.</p></div>
            </div>
        </section>
        <section class="section">
            <h2>Full Human Control</h2>
            <p>Apex AI never takes autonomous action on your behalf. It suggests, flags, and escalates — you approve or override every decision. Every AI action and human override is recorded in an immutable audit trail.</p>
            <h3>When the AI Is Uncertain</h3>
            <p>When Apex encounters ambiguous fit signals, unverifiable contacts, or conflicting data, it escalates the item with a specific explanation: what it found, why it's uncertain, and what a human should verify. Uncertainty is surfaced, not hidden.</p>
        </section>
        <section class="section">
            <h2>Integration Options</h2>
            <p>Apex AI integrates with your existing sales workflow through:</p>
            <div class="integration-grid">
                <div class="integration-card"><h4>Email Integration</h4><p>Runs through your existing email system with sending controls and reply handling.</p></div>
                <div class="integration-card"><h4>CSV / JSON Export</h4><p>Export qualified leads directly into your CRM or database via CSV or JSON.</p></div>
                <div class="integration-card"><h4>Audit Logging</h4><p>Full audit trail on every AI action, human decision, and exported record.</p></div>
                <div class="integration-card"><h4>Isolated Environments</h4><p>Each client runs in a dedicated environment with encrypted storage and strict access controls.</p></div>
            </div>
        </section>
        <section class="cta-section"><a href="contact.html" class="btn">Request Early Access</a></section>
'''

# ====== SECURITY PAGE ======
security_body = '''
        <section class="page-hero"><div><h1>Security</h1><p>How we protect your data across all Web Three Innovations products.</p></div></section>
        <section class="section">
            <h2>Data Protection</h2>
            <p>All data transmitted to and from our products is encrypted in transit using TLS 1.2 or higher. Data at rest is encrypted using AES-256. Access to customer data is strictly limited to authorized personnel with a legitimate business need.</p>
            <h3>Model Training Policy</h3>
            <p>Customer data is <strong style="color:var(--text-bright);">never</strong> used to train or improve shared AI models. Your data is isolated to your organization. We do not use your inputs to fine-tune models that other customers might access.</p>
            <h3>Data Retention</h3>
            <p>Customer data is retained according to your configured retention policy. By default, processed data is stored for 90 days, then permanently deleted. Customers can configure shorter retention windows.</p>
            <h3>Access Controls</h3>
            <p>Role-based access controls (RBAC) allow you to define who can configure campaigns, review results, approve decisions, and export data. All access events are logged.</p>
            <h3>Audit Logging</h3>
            <p>Every AI suggestion, human review decision, override, and export is logged with timestamp, user ID, and rationale. Audit logs are immutable and available to account administrators.</p>
            <h3>Infrastructure</h3>
            <p>All products are hosted on SOC 2 compliant infrastructure. Regular security assessments and penetration testing are conducted.</p>
        </section>
'''

# ====== PRIVACY PAGE ======
privacy_body = '''
        <section class="page-hero"><div><h1>Privacy Policy</h1><p>How we collect, use, and protect your data.</p></div></section>
        <section class="section">
            <p style="color:var(--text-dim); margin-bottom:2rem;"><strong style="color:var(--text-bright);">Last Updated:</strong> July 2026</p>
            <h2>1. Information We Collect</h2>
            <p>When you use our products, we collect: (a) data you provide (target company lists, campaign configurations, contact data); (b) account information (name, email, organization); (c) usage data (features used, processing volume); (d) communication records (support requests, feedback).</p>
            <h2>2. How We Use Your Information</h2>
            <p>We use your data to: provide the service you requested; improve our products based on aggregated, anonymized usage patterns; communicate about your account; respond to support requests. We do not sell your data.</p>
            <h2>3. AI Training</h2>
            <p>Your data is <strong style="color:var(--text-bright);">not</strong> used to train shared AI models. Models may be fine-tuned solely for your organization upon request, and those fine-tuned models remain isolated to your account.</p>
            <h2>4. Data Sharing</h2>
            <p>We share data only: with service providers necessary to operate the platform (cloud infrastructure, email); when required by law; with your explicit consent.</p>
            <h2>5. Data Retention & Deletion</h2>
            <p>Data is retained per your configured policy (default 90 days). You may request deletion at any time. Account data is retained while your account is active and for 30 days after closure.</p>
            <h2>6. Your Rights</h2>
            <p>You may: access your data; request correction or deletion; export your data; opt out of non-essential communications. Contact info@webthreeinnovations.com for any privacy requests.</p>
            <h2>7. Contact</h2>
            <p>For privacy questions: <a href="mailto:info@webthreeinnovations.com" style="color:var(--text-bright);">info@webthreeinnovations.com</a></p>
        </section>
'''

# ====== TERMS PAGE ======
terms_body = '''
        <section class="page-hero"><div><h1>Terms of Service</h1><p>Terms governing the use of Web Three Innovations products.</p></div></section>
        <section class="section">
            <p style="color:var(--text-dim); margin-bottom:2rem;"><strong style="color:var(--text-bright);">Last Updated:</strong> July 2026</p>
            <h2>1. Acceptance</h2>
            <p>By using Apex AI, you agree to these terms. If you are using the service on behalf of an organization, you represent that you have authority to bind that organization.</p>
            <h2>2. Service Description</h2>
            <p>Apex AI provides top-of-funnel sales development automation. The AI researches, qualifies, suggests outreach, and handles replies; it does not make autonomous decisions. You remain responsible for all decisions made using the service.</p>
            <h2>3. User Responsibilities</h2>
            <p>You agree to: provide accurate information; maintain the confidentiality of your account credentials; review AI outputs before acting on them; comply with applicable laws and regulations, including email-sending and data-protection requirements.</p>
            <h2>4. Intellectual Property</h2>
            <p>Your data and campaign configurations remain your property. We claim no ownership over your content. The Apex AI platform, software, and underlying technology are owned by Web Three Innovations.</p>
            <h2>5. Limitation of Liability</h2>
            <p>To the maximum extent permitted by law, Web Three Innovations is not liable for: decisions made based on AI outputs; indirect or consequential damages; service interruptions beyond our reasonable control.</p>
            <h2>6. Termination</h2>
            <p>Either party may terminate service with 30 days notice. Upon termination, your data will be exported or deleted per your preference within 30 days.</p>
            <h2>7. Contact</h2>
            <p>For legal inquiries: <a href="mailto:info@webthreeinnovations.com" style="color:var(--text-bright);">info@webthreeinnovations.com</a></p>
        </section>
'''

# Build all pages
pages = {
    'about.html': ('About | Web Three Innovations',
                   'Web Three Innovations builds practical software tools for enterprise operations. Learn about our team and approach.',
                   about_body),
    'contact.html': ('Request Early Access | Web Three Innovations',
                     'Request early access to Web Three Innovations products — Apex AI for sales automation, Exagent for LLM trading, and Agent Consensus for secure AI deployment.',
                     contact_body),
    'how-it-works.html': ('How It Works | Apex AI | Web Three Innovations',
                          'How Apex AI runs top-of-funnel sales automation — from target research and outreach through qualified lead handoff, under full human control.',
                          how_it_works_body),
    'security.html': ('Security | Web Three Innovations',
                      'Web Three Innovations security practices — data encryption, access controls, model training policy, and audit logging.',
                      security_body),
    'privacy.html': ('Privacy Policy | Web Three Innovations',
                     'Privacy policy for Web Three Innovations products. Learn how we collect, use, and protect your data.',
                     privacy_body),
    'terms.html': ('Terms of Service | Web Three Innovations',
                   'Terms of Service for Web Three Innovations products.',
                   terms_body),
}

for filename, (title, desc, body) in pages.items():
    html = build_dark_page(title, desc, body)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Migrated: {filename}')