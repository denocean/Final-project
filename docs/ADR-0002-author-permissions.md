# ADR-0002: Enforce Author Permissions on Edit/Delete

**Context:**
Only the author should be able to edit or delete their own posts.

**Decision:**
Use `UserPassesTestMixin` in UpdateView and DeleteView to restrict access.

**Consequences:**
- Improves security and user experience.
- Prevents unauthorized changes.
