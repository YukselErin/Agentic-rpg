import redis

class SVGBard:
    def __init__(self, redis_host='localhost', redis_port=6379):
        self.redis = redis.Redis(host=redis_host, port=redis_port, db=0)

    def get_svg(self, asset_description: str) -> str:
        cached_svg = self.redis.get(f"svg:{asset_description}")
        if cached_svg:
            return cached_svg.decode('utf-8')

        # Placeholder for LLM call to generate SVG
        new_svg = f"<svg width='100' height='100'><text>{asset_description}</text></svg>"
        
        self.redis.set(f"svg:{asset_description}", new_svg)
        return new_svg
