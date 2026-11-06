# 13. Newsletter and blog publishing assistant (job playbook)

A "Newsletter Publishing Assistant" makes sure posts go live **correct, consistent and on time**. It's an accuracy and coordination job, a good entry into content and marketing, and also a service you can sell (Tier B in `offers/02-bah-digital-service-menu.md`).

## What the work really is
| Task | What "good" looks like |
|---|---|
| Format posts to templates and style guides | Same look every time, no stray formatting |
| Double-check links, images, metadata | Nothing broken, every image has alt text, title/tags/category right |
| Upload images and set titles, tags, categories | Correct files, sensible names, small sizes |
| Track progress in spreadsheets or project tools | Anyone can see what's ready, scheduled, published |
| Coordinate with Content and Analytics teams | Clear hand-offs, no surprises |

## Your tools in this project
- `scripts/check_post.py`: finds missing metadata, broken/placeholder links, missing alt text, heading problems, repeated words. Tested with `python3 -m unittest discover -s tests`.
- `templates/newsletter-post-template.md` and `templates/newsletter-publishing-checklist.md`.
- `tracker/publishing_log.csv` (create with `bash scripts/init_tracker.sh`).
- Claude: `/publish-check <file>` to run the checks and explain results.

## A normal day
1. Open the tracker: what's scheduled today and tomorrow?
2. For each post: format -> `/publish-check` -> manual review -> preview on phone -> schedule or publish.
3. Update the log and tell Content/Analytics what's ready.
4. After publishing: open the live page, test links, record the URL.
5. Note any problem and its fix, so it never repeats (a "lessons" list).

## Learn the tools (free, 2 weeks)
| Day | Do |
|---|---|
| 1-2 | Make a free WordPress.com site (verify the free plan) and publish 3 test posts: headings, images with alt text, categories, tags, a scheduled post |
| 3-4 | Try a newsletter tool free tier (Beehiiv, MailerLite, Substack or Kit; verify limits): create a template, send a test to yourself |
| 5-6 | Learn Webflow's CMS basics from its free University lessons (verify) or Ghost; know what a CMS collection is |
| 7 | Spreadsheet skills: filters, dropdowns, conditional formatting, a publishing calendar |
| 8-9 | Practise with `check_post.py`: break a post on purpose, fix it |
| 10 | Learn UTM links (Google's campaign URL builder) and why analytics need them |
| 11-12 | Style guide practice: take a short text and apply a style (AP-style or the company's own) |
| 13-14 | Build an automation: a new row in the log Sheet sends a Slack/email alert (n8n or Make) |

## AI-aware workflow (what they ask for)
- Claude drafts the **checklist run**, spots typos and awkward links, writes alt-text suggestions, and drafts hand-off notes. A human confirms every change.
- Never let AI change the meaning of the author's text or invent facts, links or quotes.
- Never paste unpublished or confidential content into tools the company hasn't approved.
- Automate the boring parts: reminders for scheduled posts, a daily summary of what's ready, a weekly publishing report from the log.

## Interview answers you can prepare
1. **"How do you avoid errors?"** A fixed checklist, an automated checker for the mechanical issues, a phone preview, and a second look at links and numbers.
2. **"What do you do when something looks wrong?"** Stop, don't publish, tell the editor exactly what and where, suggest a fix, record it.
3. **"How do you use AI?"** To speed up checks and drafts, always with human review, never to change facts.
4. **"How do you track work?"** One log with status, date, URL and notes, updated the moment something changes.

## Pricing and growth
Employer roles like this often quote a monthly range (check currency and hours). As your own service: format-and-publish packages ($ per post or per month) or a monthly "newsletter operations" retainer. Grow into: managing multiple newsletters, analytics reports, subject-line testing, segmentation.
