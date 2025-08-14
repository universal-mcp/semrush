from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration
from typing import Any

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

    def domain_ad_history(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_filter: str | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None
    ) -> dict[str, Any]:
        """
        Get domain ad history data from Semrush API.
        
        This report shows the history of ads for a specific domain, including
        ad copies, landing pages, and performance metrics over time.
        
        Args:
            domain (str): Unique name of the website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "tr_desc", "pc_asc")
            display_filter (str, optional): Filter criteria for columns
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response
            
        Returns:
            Dict[str, Any]: API response data
            
        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails
        """
        if not domain:
            raise ValueError("Domain parameter is required")
            
        # Build parameters dictionary
        params = {
            "type": "domain_ad_history",
            "key": self.api_key,
            "domain": domain,
            "database": database
        }
        
        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if display_date is not None:
            params["display_date"] = display_date
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_filter is not None:
            params["display_filter"] = display_filter
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
            
        response = self._get(self.base_url, params=params)
        
        return self._handle_response(response)

    def domain_organic_pages(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_filter: str | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None
    ) -> dict[str, Any]:
        """
        Get domain organic pages data from Semrush API.
        
        This report shows unique pages of the analyzed domain ranking in Google's 
        top 100 organic search results.
        
        Args:
            domain (str): Unique name of the website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "tr_desc", "pc_asc")
            display_filter (str, optional): Filter criteria for columns
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response
            
        Returns:
            dict[str, Any]: API response data
            
        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails
        """
        if not domain:
            raise ValueError("Domain parameter is required")
            
        # Build parameters dictionary
        params = {
            "type": "domain_organic_unique",
            "key": self.api_key,
            "domain": domain,
            "database": database
        }
        
        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if display_date is not None:
            params["display_date"] = display_date
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_filter is not None:
            params["display_filter"] = display_filter
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
            
        response = self._get(self.base_url, params=params)
        
        return self._handle_response(response)

    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return [self.domain_ad_history, self.domain_organic_pages]
