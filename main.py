from etl.get_top_tracks import get_top_tracks
from etl.build_star_schema import build_star_schema

def run_pipeline():
    print("🎧 Starting Spotify BI pipeline...")
    
    # Step 1: Extract top tracks from Spotify
    print("🚀 Fetching top tracks from Spotify...")
    get_top_tracks()
    
    # Step 2: Transform into star schema
    print("🧱 Building star schema...")
    build_star_schema()

    print("✅ Pipeline complete! Check your /data and /star_schema_tables folders.")

if __name__ == "__main__":
    run_pipeline()
