
        # VRChatAPI: Build a mock Request object to work with
        from urllib.request import Request
        mock_request_object = Request(url=url, method=method, headers=headers)
        self.cookie_jar.add_cookie_header(mock_request_object)
        if "Cookie" in mock_request_object.unredirected_hdrs:
            headers["Cookie"] = mock_request_object.unredirected_hdrs["Cookie"]
