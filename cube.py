# Cube configuration options: https://cube.dev/docs/config

from cube import config
 
@config('semantic_layer_sync')
def semantic_layer_sync(ctx: dict) -> list[dict]:
  return [
    {
      'type': 'preset',
      'name': 'Preset Sync',
      'active': True,
      'config': {
        'database': "Cube Cloud: gcp-prod",
        'api_token': "aa8571ad-66b4-4cf2-a7d1-13480b970ad2",
        'api_secret': "215dea582d4506d220bccdcd912eeda571ba339b5193a82dc716c354c2f6d76d",
        'workspace_url': "aaad0f2c.us2a.app.preset.io"
      }
    }
  ]
