# Web Three Innovations Website Content Findings

**Review role:** Apex Engineering  
**Scope:** Independent read-only content and product-consistency review  
**Review date:** 2026-08-06  
**Change authority:** None. This report does not authorize website edits or deployment.

## Executive finding

The public website presents two materially different descriptions of Apex AI. The current home and Apex product pages describe a sales-development and sales-automation product. Several older pages still describe Apex as a document-review product. This conflict can confuse buyers, weaken trust, and send leads into an incorrect contact flow.

The site also uses two different visual and navigation systems. The newer product pages use a dark design. About, Contact, How It Works, Security, Privacy, and Terms use an older light design and older product language. The first release priority should be one accurate product position and one consistent conversion path.

## Verified findings

### 1. Critical: Apex product position is inconsistent

- The home page and `/apex-ai` describe Apex as sales automation.
- About, How It Works, Contact, Security, Privacy, and Terms contain document-review language.
- The contact flow therefore does not match the current Apex product page.

**Recommendation:** Treat the current Apex product authority as the source for all Apex statements. Replace the old document-review copy only after the owner confirms that the sales-development product is the intended public offer.

### 2. High: Product claims need evidence or qualification

The site makes detailed claims about encryption, retention, audit logs, infrastructure, security reviews, model training, sandboxing, platform support, and product performance. Some claims can be correct, but the public pages do not show the evidence or the limits of each claim.

**Recommendation:** Create a claim register. For each claim, record the product, responsible owner, evidence source, last review date, and required qualification. Remove or narrow any claim that does not have current evidence.

### 3. High: Policy pages describe the wrong workflow

Privacy, Security, and Terms focus on document upload, document processing, and document review. This does not match the current sales-development product. These pages can create legal and procurement confusion.

**Recommendation:** Ask legal and product owners to approve one current data-flow description before any policy rewrite. Do not copy sales-page language into legal pages without that review.

### 4. High: The Apex integration description is incomplete

The current Apex product page emphasizes Microsoft 365 and Classic Outlook. The live Apex product now has generic, tenant-owned Gmail support in addition to Microsoft Graph and Outlook compatibility.

**Recommendation:** Add Gmail only after the bounded production canary is complete and the owner approves the public statement. Describe provider support in a company-neutral way. Do not identify the first test client or mailbox.

### 5. Medium: The site has two navigation and design systems

- Four newer product pages use the current dark design.
- Six older pages use an older light header and different product navigation.
- The older navigation includes a `TBD` destination that does not represent a clear product.

**Recommendation:** Move the high-value conversion and trust pages to one shared header, footer, product list, and visual system. Do this after product and policy copy is approved.

### 6. Medium: Conversion routes need direct verification

- The Contact page posts to `/thank-you`, but the reviewed page inventory does not include a matching static page.
- An older navigation link targets `index.html#how-it-works`, while the current home-page section uses a different anchor.
- Email links use Cloudflare email protection. Automated review could not prove the final browser behavior.

**Recommendation:** Test the contact form, confirmation route, protected email links, and all navigation links in a real browser. Record one evidence result for each route before release.

### 7. Medium: Trust evidence is thin

The site has few published customer examples, measured results, or current case studies. One page states that accuracy metrics are published, but the reviewed public pages do not show those metrics.

**Recommendation:** Remove the promise or publish approved evidence. Do not publish customer names, metrics, or case-study files without owner approval.

### 8. Low: Brand and search foundations are incomplete

The reviewed inventory contains several logo files, inconsistent logo use, and no clear canonical favicon. It also does not show a sitemap or robots file.

**Recommendation:** Select one approved logo set and favicon. Add basic search metadata, sitemap, and robots controls after the product-page structure is final.

### 9. Low: Legacy assets need an ownership decision

The inventory includes an unused-looking legacy page and older site-builder assets.

**Recommendation:** Confirm that the live host does not use these files. Archive them before any removal. Do not delete them as part of this read-only review.

## Recommended order of work

1. Confirm the public Apex product position.
2. Correct the Contact, About, and How It Works journey.
3. Review Security, Privacy, and Terms with product and legal owners.
4. Create and verify the public-claim register.
5. Unify navigation, header, footer, logo, and visual treatment.
6. Test all links and conversion routes in a real browser.
7. Add approved proof, case studies, and measured results.
8. Clean up legacy assets only after dependency evidence exists.

## Decisions required

- Is Apex sales development the only current public Apex offer?
- When can Gmail support be named publicly?
- Which security, retention, audit, hosting, and model-training claims have approved evidence?
- Are the existing case-study files approved for public use?
- Which product owns the `TBD` navigation position?
- What system handles `/thank-you` in production?

## Out of scope

- Website edits or deployment
- Legal approval of policy language
- Publication of customer identities, results, or case studies
- Product, Gmail, Outlook, Graph, security, or infrastructure changes
- Deletion of pages or assets

## Evidence reviewed

- Public home page
- Public Apex AI, Exagent, and Agent Consensus pages
- Public About, Contact, How It Works, Security, Privacy, and Terms pages
- Current Apex product authority and tenant-isolation rules
- Current Gmail, Microsoft Graph, and Outlook production status from the controlled release record

## Acceptance for the next website revision

A future website revision should not ship until:

- all public Apex pages describe one approved product;
- policy pages match the approved data flow;
- high-risk claims have evidence and owner approval;
- the contact and confirmation routes work;
- product navigation has no placeholder destination;
- the shared header, footer, and brand assets are consistent; and
- no private client, mailbox, credential, or internal operating data is exposed.
