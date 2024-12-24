# Testing Guide

This document outlines the steps required to thoroughly test the functionality of the application with both member and admin permissions. Each command will be tested in both scenarios to ensure proper access control and functionality.

---

## General Testing Notes
1. All tests must be performed twice:
   - **Admin Permissions** first.
   - **Member Permissions** second.
2. Begin with admin permissions to ensure commands requiring admin privileges can be tested.

---

## Test Plan

### 1. **Send a Message**
- **Objective**: Verify user stats in the database.
- **Steps**:
  1. Perform the test with admin permissions.
  2. Perform the test with member permissions.
  3. Send a message.
  4. Check the database for updated user stats.

### 2. **Stats Command**
- **Objective**: Confirm the stats message is accurate.
- **Steps**:
  1. Perform the test with admin permissions.
  2. Perform the test with member permissions.
  3. Execute the stats command.
  4. Verify the returned message contains correct stats.
  5. Confirm the stats differ between member and admin.

### 3. **Make Login Rewards**
- **Objective**: Test login rewards functionality.
- **Steps**:
  1. Perform the test with admin permissions.
  2. Perform the test with member permissions.
  3. Attempt to use the command with member permissions (should fail).
  4. Use the command with admin permissions (should succeed).
  5. Verify the success message is returned.

### 4. **Login**
- **Objective**: Test login functionality and its effect on user stats.
- **Steps**:
  1. Perform the test with admin permissions.
  2. Perform the test with member permissions.
  3. Execute the login command.
  4. Confirm success messages.
  5. Check the database for updated user stats.

### 5. **Leaderboard**
- **Objective**: Verify the leaderboard display.
- **Steps**:
  1. Perform the test with admin permissions.
  2. Perform the test with member permissions.
  3. Execute the leaderboard command.
  4. Check the returned message is an embed with specific fields when converted to a dictionary.
  5. **Warning**: The correctness of leaderboard content cannot be fully verified beyond its existence.

### 6. **LevelToXp**
- **Objective**: Validate XP level calculation.
- **Steps**:
  1. Perform the test with admin permissions.
  2. Perform the test with member permissions.
  3. Use the command with member permissions (should fail).
  4. Use the command with admin permissions (should succeed).
  5. Confirm the returned message is correct.

### 7. **GenerateCard**
- **Objective**: Test card generation.
- **Steps**:
  1. Perform the test with admin permissions.
  2. Perform the test with member permissions.
  3. Attempt the command with member permissions (should fail).
  4. Use the command with admin permissions (should succeed).
  5. Verify the returned message contains an image.

### 8. **ViewCard**
- **Objective**: Test viewing user cards.
- **Steps**:
  1. Perform the test with admin permissions.
  2. Perform the test with member permissions.
  3. Attempt the command with member permissions (should fail).
  4. Use the command with admin permissions (should succeed).
  5. Verify the returned message contains an image.

### 9. **CopyCard**
- **Objective**: Test copying stats to another user.
- **Steps**:
  1. Perform the test with admin permissions.
  2. Perform the test with member permissions.
  3. Attempt the command with member permissions (should fail).
  4. Use the command with admin permissions (should succeed).
  5. Confirm the target user has the correct stats.

### 10. **Reset**
- **Objective**: Test resetting user stats.
- **Categories**:
  - XP
  - Money
  - Last Login
  - Days Logged In In A Row
- **Steps**:
  1. Perform the test with admin permissions.
  2. Perform the test with member permissions.
  3. Attempt the reset command with member permissions (should fail).
  4. Use the reset command with admin permissions (should succeed).
  5. Check the database for updated stats.
  6. Verify stats using the stats command.

### 11. **Set**
- **Objective**: Test setting specific user stats.
- **Categories**:
  - XP
  - Money
  - Last Login
  - Days Logged In In A Row
- **Steps**:
  1. Perform the test with admin permissions.
  2. Perform the test with member permissions.
  3. Attempt the set command with member permissions (should fail).
  4. Use the set command with admin permissions (should succeed).
  5. Check the database for updated stats.
  6. Verify stats using the stats command.

### 12. **Vanity**
- **Objective**: Test vanity command output.
- **Steps**:
  1. Perform the test with admin permissions.
  2. Perform the test with member permissions.
  3. Execute the vanity command.
  4. Verify the returned message is valid and correct.

---

## Final Notes
- For each test, ensure clear documentation of expected and actual results.
- Pay special attention to differences in behavior between member and admin permissions.

---

