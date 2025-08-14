from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class SemrushApp(APIApplication):
    """
    Base class for Universal MCP Applications.
    """
    def __init__(self, integration: Integration | None = None, **kwargs) -> None:
        super().__init__(name="semrush", integration=integration, **kwargs)
        self.base_url="https://api.semrush.com"
        self._api_key: str | None = None
      
    def _get_headers(self):
        if not self.integration:
            raise ValueError("Integration not found")
        credentials = self.integration.get_credentials()
        if "api_key" in credentials:
            self.api_key = credentials["api_key"]
        # Always return empty headers
        return {}

    @property
    def api_key(self):
        """Gets the API key by calling _get_headers and caches it."""
        if self._api_key:
            return self._api_key
        self._get_headers()
        return self._api_key

    @api_key.setter
    def api_key(self, value: str) -> None:
        """Sets the API key.
        
        Args:
            value (str): The API key to set.
        """
        self._api_key = value

    def domain_add_history(self):
        pass

   

    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return []
