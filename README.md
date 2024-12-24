# Testing Guide

This document outlines the steps required to thoroughly test the functionality of the application with both member and admin permissions. Each command will be tested in both scenarios to ensure proper access control and functionality.

---

## General Testing Notes
1. All tests must be performed twice:
   - **First with Admin Permissions**: Complete all tests in this guide as an admin first.
   - **Then with Member Permissions**: After completing all admin tests, repeat the entire process with member permissions.
2. Begin with admin permissions to ensure commands requiring admin privileges can be tested.

---

## Test Plan

### 1. **Send a Message**
- **Objective**: Verify user stats in the database.
- **Steps**:
  1. Send a message.
  2. Check the database for updated user stats.

### 2. **Stats Command**
- **Objective**: Confirm the stats message is accurate.
- **Steps**:
  1. Execute the stats command.
  2. Verify the returned message contains correct stats.
  3. Confirm the stats differ between member and admin.

### 3. **Make Login Rewards**
- **Objective**: Test login rewards functionality.
- **Steps**:
  1. Attempt to use the command (should fail with member permissions).
  2. Use the command (should succeed with admin permissions).
  3. Verify the success message is returned.

### 4. **Login**
- **Objective**: Test login functionality and its effect on user stats.
- **Steps**:
  1. Execute the login command.
  2. Confirm success messages.
  3. Check the database for updated user stats.

### 5. **Leaderboard**
- **Objective**: Verify the leaderboard display.
- **Steps**:
  1. Execute the leaderboard command.
  2. Check the returned message is an embed with specific fields when converted to a dictionary.
  3. **Warning**: The correctness of leaderboard content cannot be fully verified beyond its existence.

### 6. **LevelToXp**
- **Objective**: Validate XP level calculation.
- **Steps**:
  1. Use the command (should fail with member permissions).
  2. Use the command (should succeed with admin permissions).
  3. Confirm the returned message is correct.

### 7. **GenerateCard**
- **Objective**: Test card generation.
- **Steps**:
  1. Attempt the command (should fail with member permissions).
  2. Use the command (should succeed with admin permissions).
  3. Verify the returned message contains an image.

### 8. **ViewCard**
- **Objective**: Test viewing user cards.
- **Steps**:
  1. Attempt the command (should fail with member permissions).
  2. Use the command (should succeed with admin permissions).
  3. Verify the returned message contains an image.

### 9. **CopyCard**
- **Objective**: Test copying stats to another user.
- **Steps**:
  1. Attempt the command (should fail with member permissions).
  2. Use the command (should succeed with admin permissions).
  3. Confirm the target user has the correct stats.

### 10. **Reset**
- **Objective**: Test resetting user stats.
- **Categories**:
  - XP
  - Money
  - Last Login
  - Days Logged In In A Row
- **Steps**:
  1. Attempt the reset command (should fail with member permissions).
  2. Use the reset command (should succeed with admin permissions).
  3. Check the database for updated stats.
  4. Verify stats using the stats command.

### 11. **Set**
- **Objective**: Test setting specific user stats.
- **Categories**:
  - XP
  - Money
  - Last Login
  - Days Logged In In A Row
- **Steps**:
  1. Attempt the set command (should fail with member permissions).
  2. Use the set command (should succeed with admin permissions).
  3. Check the database for updated stats.
  4. Verify stats using the stats command.

### 12. **Vanity**
- **Objective**: Test vanity command output.
- **Steps**:
  1. Execute the vanity command.
  2. Verify the returned message is valid and correct.

---

## Final Notes
- For each test, ensure clear documentation of expected and actual results.
- Pay special attention to differences in behavior between member and admin permissions.

---

