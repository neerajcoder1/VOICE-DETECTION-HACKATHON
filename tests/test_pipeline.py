import sys
import os

# Add project root to PYTHONPATH so audio_pipeline can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from audio_pipeline.pipeline import pipeline_from_base64


def test_pipeline_output_shape():
    """
    Ensures pipeline never breaks downstream.
    """
    dummy_b64 = "UklGRiQAAABXQVZFZm10IBAAAAABAAEAESsAACJWAAACABAAZGF0YQAAAAA="
    out = pipeline_from_base64(dummy_b64)

    assert out.ndim == 1
    assert out.shape[0] > 0
