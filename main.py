from etl.get_top_tracks import get_top_tracks
from etl.build_star_schema import build_star_schema

def run_pipeline():
    print("🎧 Starting Spotify BI pipeline...")
    
    # Step 1: Extract top tracks from Spotify
    print("🚀 Fetching top tracks from Spotify...")
    get_top_tracks()
    
    # Step 2: Build star schema from the extracted data
    print("🧱 Building star schema tables...")
    build_star_schema()

    print("✅ Pipeline complete! Data saved to /data and /star_schema_tables.")

if __name__ == "__main__":
    run_pipeline()