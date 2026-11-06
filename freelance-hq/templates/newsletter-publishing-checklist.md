# Newsletter / blog publishing checklist (use for EVERY post)

**Post:** ____ | **Newsletter:** ____ | **Publish date/time (with time zone):** ____ | **Prepared by:** ____ | **Checked by:** ____

## 1. Before you start
- [ ] I have the final approved text (not a draft in progress) and know who approved it
- [ ] I have the style guide and the correct template for this newsletter
- [ ] I have all images with permission to use them and the credit line, if any
- [ ] I know the publish date, time and time zone

## 2. Metadata (see `scripts/check_post.py`)
- [ ] Title: clear, correct spelling, about 60 characters or less
- [ ] Meta description: 70-160 characters
- [ ] Slug: lowercase, hyphens, no dates or odd symbols
- [ ] Category and tags chosen from the approved list
- [ ] Author, date and canonical details correct
- [ ] Social share image set (if the platform has the field)

## 3. Formatting
- [ ] One H1 (the title), then H2/H3 in order
- [ ] Short paragraphs; lists and bold used the way the style guide says
- [ ] Fonts, spacing and buttons match the template
- [ ] Quotes, numbers, names and dates match the source text
- [ ] No leftover notes, "TODO", comments or placeholder text

## 4. Links
- [ ] Every link opens the right page (click each one, or run `--online`)
- [ ] Links open the right page on mobile
- [ ] Link text describes the destination (no "click here")
- [ ] UTM tags added where the analytics team asked for them
- [ ] Unsubscribe and "view in browser" links work (email only)

## 5. Images
- [ ] Every image has descriptive alt text
- [ ] File size is reasonable (not slower than the template)
- [ ] Images are not stretched or cut off, on desktop and mobile
- [ ] Image credits and licences are recorded

## 6. Preview and test
- [ ] Preview on desktop and a phone
- [ ] Send a test email to myself and the editor (email only)
- [ ] Read the whole post once aloud for typos
- [ ] A second person has checked it (if the process requires it)

## 7. Schedule and record
- [ ] Scheduled for the correct time and time zone
- [ ] Audience/segment/list is correct
- [ ] Row added to the publishing log (`tracker/publishing_log.csv`)
- [ ] Content and Analytics teams notified, with the live URL once published
- [ ] After publishing: open the live page and confirm everything works

## If something is wrong
Do not publish. Tell the editor what you found, where, and what you suggest. Record it in the log notes.
