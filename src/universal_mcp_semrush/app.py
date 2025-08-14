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
        Get domain ad history data showing past ad copies, landing pages, and performance metrics over time.
        
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

        Tags:
            domain-search, important
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
        Get unique pages of a domain that rank in Google's top 100 organic search results.
        
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

        Tags:
            domain-search
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

    def domain_organic_search_keywords(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_date: str | None = None,
        display_daily: int | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_positions: str | None = None,
        display_positions_type: str | None = None,
        display_filter: str | None = None,
        export_escape: int | None = None
    ) -> dict[str, Any]:
        """
        Get keywords that bring organic traffic to a domain via Google's top 100 search results.
        
        Args:
            domain (str): Unique name of a website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            display_date (str, optional): Date in format "YYYYMM15" or "YYYYMMDD"
            display_daily (int, optional): Set to 1 for daily updates in last 31 days
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "po_asc", "tg_desc")
            display_positions (str, optional): Filter by position changes ("new", "lost", "rise", "fall")
            display_positions_type (str, optional): Position type ("organic", "all", "serp_features")
            display_filter (str, optional): Filter criteria for columns
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            
        Returns:
            dict[str, Any]: API response data
            
        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domain:
            raise ValueError("Domain parameter is required")
            
        # Build parameters dictionary
        params = {
            "type": "domain_organic",
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
        if display_daily is not None:
            params["display_daily"] = display_daily
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_positions is not None:
            params["display_positions"] = display_positions
        if display_positions_type is not None:
            params["display_positions_type"] = display_positions_type
        if display_filter is not None:
            params["display_filter"] = display_filter
        if export_escape is not None:
            params["export_escape"] = export_escape
            
        response = self._get(self.base_url, params=params)
        
        return self._handle_response(response)

    def domain_organic_subdomains(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None
    ) -> dict[str, Any]:
        """
        Get subdomains of a domain that rank in Google's top 100 organic search results.
        
        Args:
            domain (str): Unique name of the website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "pc_asc", "tg_desc")
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response
            
        Returns:
            dict[str, Any]: API response data
            
        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domain:
            raise ValueError("Domain parameter is required")
            
        # Build parameters dictionary
        params = {
            "type": "domain_organic_subdomains",
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
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
            
        response = self._get(self.base_url, params=params)
        
        return self._handle_response(response)

    def domain_paid_search_keywords(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_date: str | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_positions: str | None = None,
        display_filter: str | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None
    ) -> dict[str, Any]:
        """
        Get keywords that bring paid traffic to a domain via Google's paid search results.
        
        Args:
            domain (str): Unique name of a website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "po_asc", "tg_desc")
            display_positions (str, optional): Filter by position changes ("new", "lost", "rise", "fall")
            display_filter (str, optional): Filter criteria for columns
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response
            
        Returns:
            dict[str, Any]: API response data
            
        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domain:
            raise ValueError("Domain parameter is required")
            
        # Build parameters dictionary
        params = {
            "type": "domain_adwords",
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
        if display_positions is not None:
            params["display_positions"] = display_positions
        if display_filter is not None:
            params["display_filter"] = display_filter
        if export_escape is not None:
            params["export_escape"] = export_escape
        if export_decode is not None:
            params["export_decode"] = export_decode
            
        response = self._get(self.base_url, params=params)
        
        return self._handle_response(response)

    def domain_pla_search_keywords(
        self,
        domain: str,
        database: str = "us",
        display_limit: int | None = None,
        display_offset: int | None = None,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_filter: str | None = None,
        export_escape: int | None = None,
        export_decode: int | None = None
    ) -> dict[str, Any]:
        """
        Get keywords that trigger a domain's product listing ads (PLA) in Google's paid search results.
        
        Args:
            domain (str): Unique name of a website to investigate
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "po_asc", "nq_desc")
            display_filter (str, optional): Filter criteria for columns
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response
            
        Returns:
            dict[str, Any]: API response data
            
        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domain:
            raise ValueError("Domain parameter is required")
            
        # Build parameters dictionary
        params = {
            "type": "domain_shopping",
            "key": self.api_key,
            "domain": domain,
            "database": database
        }
        
        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
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

    def domain_vs_domain(
        self,
        domains: str,
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
        Compare up to five domains by common keywords, unique keywords, or search terms unique to the first domain.
        
        Args:
            domains (str): URL-encoded string containing domains in format: <sign>|<type>|<domain>
                          Examples:
                          - Shared keywords: "*|or|domain1|*|or|domain2|*|or|domain3"
                          - All keywords: "*|or|domain1|+|or|domain2|+|or|domain3"
                          - Unique keywords: "*|or|domain1|-|or|domain2|-|or|domain3"
                          - Untapped keywords: "*|or|domain2|+|or|domain3|-|or|domain1"
            database (str): Regional database (default: "us")
            display_limit (int, optional): Number of results to return (max 100,000)
            display_offset (int, optional): Number of results to skip
            display_date (str, optional): Date in format "YYYYMM15" for historical data
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "p0_asc", "p1_desc")
            display_filter (str, optional): Filter criteria for columns
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            export_decode (int, optional): Set to 0 for URL-encoded response
            
        Returns:
            dict[str, Any]: API response data
            
        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            domain-search
        """
        if not domains:
            raise ValueError("Domains parameter is required")
            
        # Build parameters dictionary
        params = {
            "type": "domain_domains",
            "key": self.api_key,
            "domains": domains,
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

    def backlinks(
        self,
        target: str,
        target_type: str,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_filter: str | None = None
    ) -> dict[str, Any]:
        """
        Get backlinks data for a domain, root domain, or URL.
        
        Args:
            target (str): Root domain, subdomain, or URL of the website to investigate
            target_type (str): Type of requested target (root_domain, domain, or url)
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order (e.g., "page_ascore_desc", "last_seen_asc")
            display_limit (int, optional): Number of results to return (max 1,000,000)
            display_offset (int, optional): Number of results to skip
            display_filter (str, optional): Filter criteria for columns
            
        Returns:
            dict[str, Any]: API response data
            
        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            backlinks
        """
        if not target:
            raise ValueError("Target parameter is required")
        if not target_type:
            raise ValueError("Target_type parameter is required")
            
        # Build parameters dictionary
        params = {
            "type": "backlinks",
            "key": self.api_key,
            "target": target,
            "target_type": target_type
        }
        
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if display_filter is not None:
            params["display_filter"] = display_filter
            
        response = self._get(self.base_url, params=params)
        
        return self._handle_response(response)

    def backlinks_overview(
        self,
        target: str,
        target_type: str,
        export_columns: str | None = None,
        display_sort: str | None = None,
        display_limit: int | None = None,
        display_offset: int | None = None,
        display_filter: str | None = None
    ) -> dict[str, Any]:
        """
        Get backlinks overview summary including type, referring domains, and IP addresses.
        
        Args:
            target (str): Root domain, subdomain, or URL of the website to investigate
            target_type (str): Type of requested target (root_domain, domain, or url)
            export_columns (str, optional): Comma-separated list of columns to include
            display_sort (str, optional): Sorting order for results
            display_limit (int, optional): Number of results to return
            display_offset (int, optional): Number of results to skip
            display_filter (str, optional): Filter criteria for columns
            
        Returns:
            dict[str, Any]: API response data
            
        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            backlinks
        """
        if not target:
            raise ValueError("Target parameter is required")
        if not target_type:
            raise ValueError("Target_type parameter is required")
            
        # Build parameters dictionary
        params = {
            "type": "backlinks_overview",
            "key": self.api_key,
            "target": target,
            "target_type": target_type
        }
        
        if export_columns is not None:
            params["export_columns"] = export_columns
        if display_sort is not None:
            params["display_sort"] = display_sort
        if display_limit is not None:
            params["display_limit"] = display_limit
        if display_offset is not None:
            params["display_offset"] = display_offset
        if display_filter is not None:
            params["display_filter"] = display_filter
            
        response = self._get(self.base_url, params=params)
        
        return self._handle_response(response)

    def keyword_difficulty(
        self,
        phrase: str,
        database: str = "us",
        export_columns: str | None = None,
        export_escape: int | None = None
    ) -> dict[str, Any]:
        """
        Get keyword difficulty data to estimate ranking difficulty for organic search terms.
        
        Args:
            phrase (str): Phrase (from 1 to 100 keywords separated by semicolons)
            database (str): Regional database (default: "us")
            export_columns (str, optional): Comma-separated list of columns to include
            export_escape (int, optional): Set to 1 to wrap columns in quotes
            
        Returns:
            dict[str, Any]: API response data
            
        Raises:
            ValueError: If required parameters are missing
            httpx.HTTPStatusError: If the API request fails

        Tags:
            keyword-analysis
        """
        if not phrase:
            raise ValueError("Phrase parameter is required")
            
        # Build parameters dictionary
        params = {
            "type": "phrase_kdi",
            "key": self.api_key,
            "phrase": phrase,
            "database": database
        }
        
        if export_columns is not None:
            params["export_columns"] = export_columns
        if export_escape is not None:
            params["export_escape"] = export_escape
            
        response = self._get(self.base_url, params=params)
        
        return self._handle_response(response)

    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return [self.domain_ad_history, self.domain_organic_pages, self.domain_organic_search_keywords, self.domain_organic_subdomains, self.domain_paid_search_keywords, self.domain_pla_search_keywords, self.domain_vs_domain, self.backlinks, self.backlinks_overview, self.keyword_difficulty]
