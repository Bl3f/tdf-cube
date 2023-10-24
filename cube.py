# Cube configuration options: https://cube.dev/docs/config

from cube import config
import os
 
@config('semantic_layer_sync')
def semantic_layer_sync(ctx: dict) -> list[dict]:
  return [
    {
      'type': 'preset',
      'name': 'Preset Sync',
      'active': True,
      'config': {
        'database': "Cube Cloud: gcp-prod",
        'api_token': os.getenv("PRESET_TOKEN"),
        'api_secret': os.getenv("PRESET_SECRET"),
        'workspace_url': "aaad0f2c.us2a.app.preset.io"
      }
    }
  ]
