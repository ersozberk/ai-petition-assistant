// frontend/e2e/petition.spec.ts
import { test, expect } from '@playwright/test';

test('Kullanıcı başarıyla dilekçe oluşturabilmeli', async ({ page }) => {
  // 1. Ana sayfaya git (Docker üzerinde çalıştığı için localhost:3000)
  await page.goto('http://localhost:3000');

  // 2. Başlığın doğru olduğunu kontrol et
  await expect(page.locator('h1')).toContainText('AI Dilekçe Asistanı');

  // 3. Form alanlarını doldur
  await page.fill('input[placeholder*="X Kargo"]', 'Test Kargo A.Ş.');
  await page.fill('textarea[placeholder*="Yaşadığınız mağduriyeti"]', 
    '15.10.2025 tarihinde aldığım ürün kırık geldi, iade kabul edilmiyor. T.C. No: 11111111110');

  // 4. "Dilekçeyi Oluştur" butonuna tıkla
  await page.click('button:has-text("Dilekçeyi Oluştur")');

  // 5. Yükleme durumunun geçtiğini ve dilekçenin geldiğini bekle (Timeout: 30sn)
  const petitionResult = page.locator('text=Taslak Dilekçeniz');
  await expect(petitionResult).toBeVisible({ timeout: 30000 });

  // 6. Yazdır butonunun orada olduğunu doğrula
  const printButton = page.locator('button:has-text("Yazdır")');
  await expect(printButton).toBeVisible();
});