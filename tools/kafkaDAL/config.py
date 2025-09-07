import os
from typing import Optional

# # Basic connection
# KAFKA_BROKER: str = os.getenv("KAFKA_BROKER", "localhost:9092")

# # Sensible defaults for examples
# KAFKA_TOPIC: str = os.getenv("KAFKA_TOPIC", "demo-topic")
# KAFKA_GROUP_ID: str = os.getenv("KAFKA_GROUP_ID", "demo-group")
# KAFKA_CLIENT_ID: str = os.getenv("KAFKA_CLIENT_ID", "kafka-dal-client")

# # Serialization format: "json" or "raw"
# KAFKA_VALUE_FORMAT: str = os.getenv("KAFKA_VALUE_FORMAT", "json").lower()
# KAFKA_KEY_FORMAT: str = os.getenv("KAFKA_KEY_FORMAT", "raw").lower()

# # TLS / SASL placeholders (extend as needed)
# SASL_MECHANISM: Optional[str] = os.getenv("KAFKA_SASL_MECHANISM")
# SASL_USERNAME: Optional[str] = os.getenv("KAFKA_SASL_USERNAME")
# SASL_PASSWORD: Optional[str] = os.getenv("KAFKA_SASL_PASSWORD")
# SECURITY_PROTOCOL: str = os.getenv("KAFKA_SECURITY_PROTOCOL", "PLAINTEXT")

# # Consumer behavior
# AUTO_OFFSET_RESET: str = os.getenv("KAFKA_AUTO_OFFSET_RESET", "earliest")  # or "latest"
# ENABLE_AUTO_COMMIT: bool = os.getenv("KAFKA_ENABLE_AUTO_COMMIT", "true").lower() == "true"
