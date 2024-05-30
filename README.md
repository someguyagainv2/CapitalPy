# CapitalPy

<h1>Capital.py API</h1>

This is a module for python for ease-of-use of the capital.py endpoints and you are able to connect this API to modern applications to check for certain things from anywhere you can use this API for bots to notify you of certain things, Capital.py is a project made by me of my own back as I support https://capital.com.

<body>

    <h1><code>accounts</code> Class Documentation</h1>

    <h2>Overview</h2>
    <p>The <code>accounts</code> class provides an interface to interact with a Capital account through its API. It allows users to perform various operations such as retrieving account information, updating preferences, and managing leverages.</p>

    <h2>Installation</h2>
    <p>To use the <code>accounts</code> class, you need to have the <code>requests</code> library installed. If you don't have it installed, you can do so using pip:</p>
    <pre><code>pip install requests</code></pre>

    <h2>Usage</h2>
    <h3>Importing the Class</h3>
    <pre><code>import requests
from accounts import accounts</code></pre>

    <h3>Initializing the Class</h3>
    <p>To create an instance of the <code>accounts</code> class, you need to provide session information (typically in the form of headers). The session information is used to authenticate requests to the API.</p>
    <pre><code>sessionInformation = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

acc = accounts(sessionInformation)</code></pre>

    <h3>Methods</h3>

    <h4><code>amount()</code></h4>
    <p>Returns the number of accounts associated with your session.</p>
    <p><strong>Usage:</strong></p>
    <pre><code>number_of_accounts = acc.amount()
print(number_of_accounts)</code></pre>

    <h4><code>returnall()</code></h4>
    <p>Returns a JSON object containing all account information.</p>
    <p><strong>Usage:</strong></p>
    <pre><code>all_accounts = acc.returnall()
print(all_accounts)</code></pre>

    <h4><code>getinfo()</code></h4>
    <p>Returns detailed information about all account parameters.</p>
    <p><strong>Usage:</strong></p>
    <pre><code>account_info = acc.getinfo()
print(account_info)</code></pre>

    <h4><code>leverages()</code></h4>
    <p>Returns information about all leverages.</p>
    <p><strong>Usage:</strong></p>
    <pre><code>leverages_info = acc.leverages()
print(leverages_info)</code></pre>

    <h4><code>getshares()</code></h4>
    <p>Returns information about share leverages.</p>
    <p><strong>Usage:</strong></p>
    <pre><code>shares_info = acc.getshares()
print(shares_info)</code></pre>

    <h4><code>getcurrencies()</code></h4>
    <p>Returns information about currency leverages.</p>
    <p><strong>Usage:</strong></p>
    <pre><code>currencies_info = acc.getcurrencies()
print(currencies_info)</code></pre>

    <h4><code>getindices()</code></h4>
    <p>Returns information about indices leverages.</p>
    <p><strong>Usage:</strong></p>
    <pre><code>indices_info = acc.getindices()
print(indices_info)</code></pre>

    <h4><code>getcrypto()</code></h4>
    <p>Returns information about cryptocurrency leverages.</p>
    <p><strong>Usage:</strong></p>
    <pre><code>crypto_info = acc.getcrypto()
print(crypto_info)</code></pre>

    <h4><code>getcommodities()</code></h4>
    <p>Returns information about commodity leverages.</p>
    <p><strong>Usage:</strong></p>
    <pre><code>commodities_info = acc.getcommodities()
print(commodities_info)</code></pre>

    <h4><code>update(newPreferences)</code></h4>
    <p>Updates account preferences with the provided JSON object.</p>
    <p><strong>Parameters:</strong></p>
    <ul>
        <li><code>newPreferences</code> (dict): A dictionary containing the new preferences.</li>
    </ul>
    <p><strong>Usage:</strong></p>
    <pre><code>new_preferences = {
    "leverages": {
        "SHARES": 5,
        "CURRENCIES": 10,
        // ... other preferences
    }
}

update_response = acc.update(newPreferences=new_preferences)
print(update_response)</code></pre>

    <h4><code>updatedemo(amount)</code></h4>
    <p>Updates the demo account balance to the specified amount.</p>
    <p><strong>Parameters:</strong></p>
    <ul>
        <li><code>amount</code> (int, optional): The new balance amount. Default is 1000.</li>
    </ul>
    <p><strong>Usage:</strong></p>
    <pre><code>demo_update_successful = acc.updatedemo(amount=5000)
print(demo_update_successful)</code></pre>

    <h2>Exception Handling</h2>
    <p>The <code>accounts</code> class raises <code>ValueError</code> exceptions when an error occurs, such as when session information or new preferences are empty, or when API requests return an error status code. Make sure to handle these exceptions in your code:</p>
    <pre><code>try:
    acc = accounts(sessionInformation)
    print(acc.amount())
except ValueError as e:
    print(f"Error: {e}")</code></pre>

    <h2>License</h2>
    <p>This project is licensed under the MIT License.</p>

</body>
</html>
