
GitHub Commits
--------------

This data source provides commits for the given repository in GitHub.

- **Source:** `GitHub Repo Commits API <http://developer.github.com/v3/repos/commits/>`_

- **Historical data:** 1000 newest commits.

- **Retention:** All commits are retained for all plans.

- **Schema:**
    .. code-block:: python

         {
             "commits": commits
         }

    where *commits* is a :mod:`bitdeli.lazylist` containing raw commit objects
    from the `GitHub Repo Commits API
    <http://developer.github.com/v3/repos/commits/>`_.

- **Update interval:** 15 minutes.

- **Code:** `bitdeli/profile-github-commits <https://github.com/bitdeli/profile-github-commits>`_
