#!/usr/bin/env python3
"""
Script to trigger a backend update on Render
"""

import requests
import time

def test_backend():
    """Test if backend is working"""
    try:
        response = requests.get('https://al-aqsabackend-1-pv0k.onrender.com/api/contact/')
        if response.status_code == 200:
            print("✅ Backend is working!")
            return True
        else:
            print(f"❌ Backend returned status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error testing backend: {e}")
        return False

def main():
    print("🔄 Testing backend after CORS update...")
    
    # Wait a moment for any potential restart
    time.sleep(5)
    
    if test_backend():
        print("🎉 Backend is ready!")
        print("📝 CORS settings updated to include:")
        print("   - https://al-aqsamedical-lab.vercel.app")
        print("   - https://al-aqsa-medical-lab.vercel.app") 
        print("🧪 You can now test the contact form!")
    else:
        print("⚠️  Backend may need a few more minutes to restart")
        print("🔄 Try testing the form in 2-3 minutes")

if __name__ == "__main__":
    main()
