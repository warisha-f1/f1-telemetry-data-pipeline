import fastf1
import os
import logging

# Setup basic logging for your Agent's Observability
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Enable caching to speed up your pipeline
if not os.path.exists('f1_cache'):
    os.makedirs('f1_cache')
fastf1.Cache.enable_cache('f1_cache')

def extract_f1_data(year, gp_name, session_type='R'):
    """
    Agent to extract raw F1 session data.
    :param year: int (e.g., 2024)
    :param gp_name: str (e.g., 'Monaco')
    :param session_type: str ('R' for Race, 'Q' for Qualifying)
    """
    logger.info(f"Extractor Agent: Fetching {year} {gp_name} Grand Prix data...")
    
    try:
        # Load the session metadata
        session = fastf1.get_session(year, gp_name, session_type)
        
        # Pull the specific data needed for your LAPS and TELEMETRY tables
        session.load(laps=True, telemetry=True, weather=False)
        
        logger.info(f"Data extracted! Found {len(session.laps)} laps.")
        return session
    except Exception as e:
        logger.error(f"Failed to extract data: {e}")
        return None

if __name__ == "__main__":
    # Test the agent with a sample 2024 race
    sample_data = extract_f1_data(2024, 'Bahrain')