import java.net.MalformedURLException;
import java.net.URL;

import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;

public class Browser {
	
	public static RemoteWebDriver getDriver(String browser) throws MalformedURLException {
		return new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), getBrowserCapabilities(browser));
	}
	
	private static DesiredCapabilities getBrowserCapabilities(String browserType) {
		switch (browserType) {
		//case "firefox":
		//	System.out.println("Opening firefox driver");
		//	return DesiredCapabilities.firefox();
		case "chrome":
			System.out.println("Opening chrome driver");
			return DesiredCapabilities.chrome();
		//case "IE":
		//	System.out.println("Opening IE driver");
		//	return DesiredCapabilities.internetExplorer();
		default:
			System.out.println("browser : " + browserType + " is invalid, Launching Chrome as browser of choice..");
			return DesiredCapabilities.chrome();
		}
	}
}
We will call 'getDriver' method which will intern call 'getBrowserCapabilities' based on browser parameter from the below two classes. If we pass 'chrome' as parameter, it is invoke chromedriver

Let us create a class as 'ParallelTestA.java' as below:
package com.test;

import java.net.MalformedURLException;

import org.openqa.selenium.remote.RemoteWebDriver;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class ParallelTestA {
	
	public static RemoteWebDriver driver;
	public static String appURL = "http://www.google.com";
	
	@BeforeClass
	@Parameters({ "browser" })
	public void setUp(String browser) throws MalformedURLException {
		System.out.println("*******************");
		driver = Browser.getDriver(browser);
		driver.manage().window().maximize();
	}
	
	@Test
	public void testGooglePageTitleInFirefox() {
		driver.navigate().to(appURL);
		String strPageTitle = driver.getTitle();
		Assert.assertTrue(strPageTitle.equalsIgnoreCase("Google"), "Page title doesn't match");
	}

	@AfterClass
	public void tearDown() {
		if(driver!=null) {
			System.out.println("Closing browser");
			driver.quit();
		}
	}
	
}
Let us create a class as 'ParallelTestB.java' as below:
package com.test;

import java.net.MalformedURLException;

import org.openqa.selenium.By;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class ParallelTestB {
		
	public static RemoteWebDriver driver;
	public static String appURL = "http://www.google.com";
	
	@BeforeClass
	@Parameters({ "browser" })
	public void setUp(String browser) throws MalformedURLException {
		System.out.println("*******************");
		driver = Browser.getDriver(browser);
		driver.manage().window().maximize();
	}
	
	@Test
	public void testGooglePageTitleInChrome() {
		driver.navigate().to("http://www.google.com");
		String strPageTitle = driver.getTitle();
		Assert.assertTrue(strPageTitle.equalsIgnoreCase("Google"), "Page title doesn't match");
	}
	
	@Test
	public void testSearchGoogle() {
		System.out.println("Opening Google..");
		driver.navigate().to(appURL);
		driver.findElement(By.name("q")).sendKeys("Selenium Easy Grid Tutorials");
		driver.findElement(By.name("btnG")).click();
	}

	@AfterClass
	public void tearDown() {
		if(driver!=null) {
			System.out.println("Closing browser");
			driver.quit();
		}
	}
}