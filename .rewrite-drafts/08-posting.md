## 8. Posting and profile (approved by the user on 18 Nov 2026 unless marked)

### 8.1 TikTok, every video
- **Caption:** the question the video answers, with one emoji, then `#HowItWorks #Engineering #LearnOnTikTok #3DAnimation` and one or
  two topic tags.
- **The hashtags must turn into links.** From video 02 on, none of ours registered (TikTok saw plain text; 1.5, 9.1). Type each tag
  in the app, or tap it from the suggestion list after typing "#", and check that it shows as a link before posting. After
  posting, check from a session that `textExtra` is not empty (12.1).
- **AI label:** TikTok has added its own AI-generated label to our videos (9 of 10, seawater included), and it didn't stop seawater.
  Turn on "AI-generated content" when posting, as TikTok's rules ask for realistic AI scenes.
- **Cover:** TikTok Studio on desktop → Edit cover → upload the 1080×1440 crop (7.6); otherwise pick the most satisfying frame.
- **Pin a comment** with the comment question; reply to every comment in the first day.
- **When:** early evening, US Eastern (our two best went out at about 6–7 pm ET). At most one video a day; never two a few hours
  apart (videos 08 and 09 went out 2.4 h apart and split their first tests).
- Don't delete a video that stalls. For the re-cut test (2.2), set the old version to private when the new one goes up.

### 8.2 YouTube Shorts, every video
- **Title:** the question the video answers, under ~60 characters, no hashtags, no call to action.
- **Description:** two or three sentences that retell the premise with the named problems, one question for the comments, then at
  most three hashtags.
- **Audience:** "No, it's not made for kids" on the upload, and as the channel default (made-for-kids mode killed video 02 at
  7 views until it was fixed).
- **Altered or synthetic content: leave it unticked** for these cutaways. YouTube's own announcement exempts clearly unrealistic
  content such as animation, and a set sliced open like a cake can't be taken for footage; no source says the label changes reach
  (18 Nov 2026). Tick it only if a video ever shows a realistic scene that could pass for real footage of a real event or person.
- **Cover:** pick the frame yourself at upload (custom covers need the Partner Program): the most satisfying cutaway moment, with
  no stray caption word on it (ours have shown "WAY", "So", "COLORS").
- **Pin the comment question**; reply to every comment in the first day.
- Post the same day as TikTok.

### 8.3 Profile fixes (do these before the first of the ten)
- **Rename the TikTok account** to match the content and the YouTube channel: the handle @overthinkingyearly tells a visitor
  nothing (the display name changed from "OT" to "overthinkingyearly" on 18 Nov 2026; the handle hasn't). The natural pick is the
  YouTube name: check that `@letzbuildtogether` is free with `pipeline/youtube/handles.py <dir> tt letzbuildtogether`. TikTok
  allows a username change once every 30 days.
- **Bio on both platforms:** what you post and how often, in one line, e.g. "The hidden inside of everyday things, in 3D. New video
  every other day."
- **Pin the three best TikTok videos:** seawater, the hydrant, and the best of the new ones as it emerges.
- Optional (not yet decided by the user): the YouTube avatar and banner still show the retired mascot and "ONE PROBLEM AT A TIME"
  (made 10 Nov 2026; files and rebuild scripts in `branding/` and `pipeline/branding/`). A cutaway frame would match the videos.

### 8.4 After posting
- Read the views at about 24 h and 72 h on both platforms (12.1, 12.2) and add them to the video log (9.2).
- **The bars:** more than ~2K on TikTok within 72 h means it passed the first test (our failed ones stop at 330–454); more than ~1K
  on YouTube means it was tested normally; 10K+ is a breakout for us.

---
