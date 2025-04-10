import pandas as pd
import os

def build_star_schema():
    # Load your top tracks CSV file (update the path if needed)
    csv_path = "data/top_tracks.csv"
    df = pd.read_csv(csv_path)

    # Create surrogate keys
    df['artist_id'] = df['Artist'].astype('category').cat.codes + 1
    df['album_id'] = df['Album'].astype('category').cat.codes + 1
    df['track_id'] = df['Track'].astype('category').cat.codes + 1

    # =========================
    # Create Dimension Tables
    # =========================

    # Dim_Artist
    dim_artist = df[['artist_id', 'Artist']].drop_duplicates().rename(columns={
        'Artist': 'artist_name'
    })

    # Dim_Album
    dim_album = df[['album_id', 'Album']].drop_duplicates().rename(columns={
        'Album': 'album_name'
    })

    # Dim_Date
    df['Release Date'] = pd.to_datetime(df['Release Date'])
    dim_date = df[['Release Date']].drop_duplicates()
    dim_date['date_id'] = dim_date['Release Date'].astype('category').cat.codes + 1
    dim_date['year'] = dim_date['Release Date'].dt.year
    dim_date['month'] = dim_date['Release Date'].dt.month
    dim_date['day'] = dim_date['Release Date'].dt.day
    dim_date = dim_date[['date_id', 'Release Date', 'year', 'month', 'day']]

    # =========================
    # Create Fact Table
    # =========================

    fact_track = df.merge(dim_date, on='Release Date')
    fact_track = fact_track[['track_id', 'artist_id', 'album_id', 'date_id', 'Popularity']]
    fact_track = fact_track.rename(columns={'Popularity': 'popularity'})

    # =========================
    # Save to CSV files
    # =========================

    dim_artist.to_csv(f"star_schema_tables/Dim_Artist.csv", index=False)
    dim_album.to_csv(f"star_schema_tables/Dim_Album.csv", index=False)
    dim_date.to_csv(f"star_schema_tables/Dim_Date.csv", index=False)
    fact_track.to_csv(f"star_schema_tables/Fact_TrackPopularity.csv", index=False)

    print("✅ Star schema tables generated successfully!")

if __name__ == "__main__":
    build_star_schema()
