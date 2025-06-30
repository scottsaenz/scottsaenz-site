"""
MkDocs Macros for Scott Saenz Site
"""

def define_env(env):
    """
    This is the hook for defining macros, variables and filters
    """
    
    @env.macro
    def podcast_icons(spotify_url, apple_url=None, youtube_url=None, website_url=None):
        """
        Generate podcast platform icons with links
        
        Args:
            spotify_url: URL to Spotify episode (required)
            apple_url: URL to Apple Podcasts episode (optional)
            youtube_url: URL to YouTube episode (optional) 
            website_url: URL to podcast website episode (optional)
        """
        icons = []
        
        # Spotify (always present)
        spotify_html = f'''[![Spotify](../src/imgs/Spotify_Primary_Logo_White_CMYK.svg){{width=21px .spotify-dark}}]({spotify_url})[![Spotify](../src/imgs/Spotify_Primary_Logo_Black_CMYK.svg){{width=21px .spotify-light}}]({spotify_url})'''
        icons.append(spotify_html)
        
        # Apple Podcasts (optional)
        if apple_url:
            apple_html = f'''[![Apple Podcasts](../src/imgs/Apple_Podcasts_Icon_RGB_sm_060623.svg){{width=21px}}]({apple_url})'''
            icons.append(apple_html)
        
        # YouTube (optional)
        if youtube_url:
            youtube_html = f'''[![YouTube](../src/imgs/YouTube_full-color_icon_(2024).svg){{width=21px}}]({youtube_url})'''
            icons.append(youtube_html)
        
        # Website (optional)
        if website_url:
            website_html = f'''[![Real Python Website](../src/imgs/python-logo-only.svg){{width=21px}}]({website_url})'''
            icons.append(website_html)
        
        # Join with spacing
        return '&nbsp;&nbsp;'.join(icons)
    
    @env.macro
    def listen_on(spotify_url, apple_url=None, youtube_url=None, website_url=None):
        """
        Complete "Listen on:" section with podcast icons
        """
        icons = podcast_icons(spotify_url, apple_url, youtube_url, website_url)
        return f"**Listen on:**\n{icons}"
