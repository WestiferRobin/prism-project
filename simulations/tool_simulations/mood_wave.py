import uvicorn
from fastapi import FastAPI

mood_api = FastAPI()


def test_mood_wave_engine():
    # 1. Discover Trending Topics
    # trends = scan_trending_data(platforms=["YouTube", "Twitter", "Instagram"],
    #                             niche="spirituality, self-help, AI, mysticism")

    # 2. Generate Script Based on Trends
    # daily_topic = choose_topic(trends, persona="Mystic Sage")
    # script = generate_ai_conversation(topic=daily_topic, tone="wise, poetic, mystical",
    #                                   characters=["PaulAI", "SolomanAI"])

    # 3. Generate Visuals and Audio
    # images = generate_aesthetic_images(script, style="spiritual, cosmic, calm")
    # voiceover = generate_voice(script, speakers=["PaulAI", "SolomanAI"])

    # 4. Create Short Videos (TikTok, Shorts, Reels)
    # short_clips = compile_video_snippets(images, voiceover, format="short", style="smooth zoom, subtitle overlay")
    # post_to_platforms(short_clips, platforms=["YouTube Shorts", "Instagram Reels", "Twitter"], schedule="1-2x/day")

    # 5. Create Podcast-Style Full Video
    # podcast_video = compile_full_convo_video(script, voiceover, background="animated temple, soft stardust flow")
    # upload_to_youtube(video=podcast_video, title=daily_topic,
    #                   tags=["Paul Soloman", "Mystic Sage", "AI podcast", "wisdom"])

    return "MOOD WAVE!!!"

@mood_api.get("/mood/test")
async def test_mood_wave():
    return "MOOD WAVE!!!!!"

def run_mood_wave(is_endpoint=False):
    if is_endpoint:
        uvicorn.run(mood_api, host="127.0.0.1", port=8000)
    else:
        test_mood_wave_engine()
