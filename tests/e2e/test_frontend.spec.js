const { test, expect } = require('@playwright/test');

test.describe('AI Empower Heart E2E Tests', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:3000');
  });

  test('should show all guru options on homepage', async ({ page }) => {
    await expect(page.locator('text=Karma Guru')).toBeVisible();
    await expect(page.locator('text=Bhakti Guru')).toBeVisible();
    await expect(page.locator('text=Meditation Guru')).toBeVisible();
    await expect(page.locator('text=Yoga Guru')).toBeVisible();
  });

  test('should be able to chat with a guru', async ({ page }) => {
    // Select Karma Guru
    await page.click('text=Karma Guru');
    
    // Type a message
    await page.fill('textarea[placeholder*="message"]', 'What is karma yoga?');
    await page.click('button:has-text("Send")');
    
    // Wait for and verify response
    const response = await page.waitForSelector('.guru-response');
    expect(await response.isVisible()).toBeTruthy();
  });

  test('should allow user registration and login', async ({ page }) => {
    // Go to register page
    await page.click('text=Register');
    
    // Fill registration form
    await page.fill('input[name="username"]', 'testuser');
    await page.fill('input[name="email"]', 'test@example.com');
    await page.fill('input[name="password"]', 'testpass123');
    await page.click('button[type="submit"]');
    
    // Verify successful registration
    await expect(page.locator('text=Registration successful')).toBeVisible();
    
    // Login
    await page.click('text=Login');
    await page.fill('input[name="email"]', 'test@example.com');
    await page.fill('input[name="password"]', 'testpass123');
    await page.click('button[type="submit"]');
    
    // Verify successful login
    await expect(page.locator('text=Dashboard')).toBeVisible();
  });

  test('should track meditation sessions', async ({ page }) => {
    // Login first
    await test.step('Login', async () => {
      await page.click('text=Login');
      await page.fill('input[name="email"]', 'test@example.com');
      await page.fill('input[name="password"]', 'testpass123');
      await page.click('button[type="submit"]');
    });

    // Go to meditation section
    await page.click('text=Meditation');
    
    // Start a session
    await page.click('text=Start Session');
    
    // Wait for 5 seconds
    await page.waitForTimeout(5000);
    
    // End session
    await page.click('text=End Session');
    
    // Verify session was recorded
    await expect(page.locator('text=Session completed')).toBeVisible();
  });
});
