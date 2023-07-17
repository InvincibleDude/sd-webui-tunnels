from pycloudflared import try_cloudflare

from modules.shared import cmd_opts
from installer import log

from gradio import strings

import os

if cmd_opts.cloudflared:
    log.info("cloudflared detected, trying to connect...")
    port = cmd_opts.port if cmd_opts.port else 7860
    tunnel_url = try_cloudflare(port=port, verbose=False)
    os.environ['webui_url'] = tunnel_url.tunnel
    colab_url = os.getenv('colab_url')
    log.info(f"Cloudflared Public WebUI Colab URL: {tunnel_url.tunnel}")
