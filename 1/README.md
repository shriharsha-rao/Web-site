# User Registration and Login System

This is a complete user management system with registration, login, a separate admin dashboard website, and URL code generation for sharing.

## Features

### 🔐 User Authentication
- **User Registration**: Users can create new accounts with username, email, and password
- **User Login**: Secure login with email and password validation
- **Session Management**: Automatic session handling and logout functionality

### 📊 Admin Dashboard (Separate Website)
- **Standalone Website**: Completely separate from the main login page
- **Admin Authentication**: Requires admin credentials (admin/admin123)
- **User Statistics**: Total users, total logins, active users, and new users
- **User Management**: View all registered users with their details
- **Login History**: Track all user login attempts and timestamps
- **Search & Filter**: Search through users and login history
- **Data Export**: Export all user data to JSON format
- **User Deletion**: Remove users from the system

### 🔗 URL Code Generation & Sharing
- **Create Shareable Codes**: Generate unique URL codes for system access
- **Customizable Codes**: Set titles, usage limits, expiry dates, and custom messages
- **Access Control**: Limit usage count and set expiration dates
- **Code Management**: Activate/deactivate codes, track usage, and manage all codes
- **Direct Access**: Users can access system directly through `access.html` with codes
- **Usage Tracking**: Monitor how many times each code is used

### 🛡️ Security Features
- **Duplicate Prevention**: Prevents registration with existing email/username
- **Session Validation**: Ensures only authenticated users access protected pages
- **Data Persistence**: All data stored in browser localStorage
- **Separate Admin Access**: Admin dashboard is completely isolated
- **Code Validation**: URL codes are validated for expiry and usage limits

## How It Works

### 1. User Registration Flow
1. User visits `index.html`
2. Clicks "Register" to open registration form
3. Fills in username, email, and password
4. System checks for duplicate users
5. If successful, user is redirected to login form

### 2. User Login Flow
1. User enters email and password
2. System validates credentials against registered users
3. If valid, user is redirected to `index1.html`
4. Login history is recorded with timestamp

### 3. Admin Dashboard Access (Separate Website)
1. **Direct Access**: Navigate directly to `dashboard.html`
2. **Admin Login**: Use credentials (username: admin, password: admin123)
3. **View Data**: Access all user statistics and management features
4. **Create URL Codes**: Generate shareable access codes for users
5. **No Connection**: Completely separate from the main user system

### 4. URL Code Access Flow
1. **Admin Creates Code**: Generate URL code with custom settings
2. **Share Code**: Send code to users via email, messaging, etc.
3. **User Enters Code**: Visit `access.html` and enter the code
4. **Code Validation**: System checks expiry, usage limits, and validity
5. **System Access**: Validated users can proceed to main system
6. **Usage Tracking**: System records each code usage

## File Structure

- `index.html` - Main login/registration page (for regular users)
- `index1.html` - Protected content page (Amazon-style interface)
- `dashboard.html` - **Separate admin website** for user management
- `access.html` - **New file** for URL code access
- `server.js` - JavaScript logic for user authentication and data handling
- `style.css` - Styling for the main page
- `styl.css` - Styling for the protected content page

## Data Storage

All user data is stored in the browser's localStorage:
- `users` - Array of registered user objects
- `loginHistory` - Array of login attempt records
- `urlCodes` - Array of generated URL codes with usage tracking

## Usage Instructions

### For Regular Users:
1. **Option 1**: Open `index.html` → Register/Login → Access content
2. **Option 2**: Get URL code from admin → Visit `access.html` → Enter code → Access system

### For Programmers/Admins:
1. **Navigate directly to `dashboard.html`** (separate website)
2. **Login with admin credentials**: username: `admin`, password: `admin123`
3. **Create URL Codes**: Generate shareable codes with custom settings
4. **Monitor Usage**: Track how many times each code is used
5. **Manage Codes**: Activate, deactivate, or delete codes as needed
6. **User Management**: View all users, login history, and statistics

## URL Code Features

### **Code Creation Options:**
- **Custom Code**: Set your own code (e.g., WELCOME2024, INVITE123)
- **Title**: Add descriptive title for the code
- **Usage Limits**: Set maximum number of uses (0 = unlimited)
- **Expiry Date**: Set when the code expires
- **Custom Message**: Add personalized message for users

### **Code Management:**
- **Activate/Deactivate**: Enable or disable codes instantly
- **Usage Tracking**: Monitor how many times each code is used
- **Expiry Management**: Automatic expiry checking
- **Search & Filter**: Find specific codes quickly
- **Export Data**: Download all code information

### **User Experience:**
- **Easy Access**: Simple code entry interface
- **Real-time Validation**: Immediate feedback on code validity
- **Code Information**: See code details before proceeding
- **Seamless Integration**: Direct access to main system after validation

## Key Changes Made

- ✅ **Admin Dashboard is now completely separate** from the main login page
- ✅ **No Admin Dashboard link** appears on the main user interface
- ✅ **Direct access** to `dashboard.html` required for admin functions
- ✅ **Separate authentication** system for admin access
- ✅ **Isolated functionality** - admin and user systems are independent
- ✅ **URL Code Generation** - Create shareable access codes
- ✅ **Code Management** - Track usage, set limits, manage expiry
- ✅ **Direct Access System** - Users can enter via `access.html` with codes

## Security Notes

- This is a client-side demo system using localStorage
- In production, implement server-side authentication
- Passwords should be hashed before storage
- Use HTTPS for secure data transmission
- Implement proper session management on the server
- **Admin dashboard is now completely isolated** from user system
- **URL codes provide controlled access** with usage limits and expiry

## Browser Compatibility

- Modern browsers with localStorage support
- JavaScript enabled
- CSS Grid and Flexbox support for layout

## Testing the System

### User System:
1. Open `index.html` in a web browser
2. Register a new user account
3. Login with the registered credentials
4. Access the protected content

### Admin System (Separate):
1. **Navigate directly to `dashboard.html`**
2. Login with admin credentials (admin/admin123)
3. **Create URL codes** with custom settings
4. View all user data and statistics
5. Test admin functions (search, export, delete)

### URL Code System:
1. **Admin creates URL code** in dashboard
2. **Share code** with users
3. **Users visit `access.html`**
4. **Enter code** and get validated
5. **Access main system** through code

## Admin Credentials

- **Username**: `admin`
- **Password**: `admin123`
- **Access**: Direct navigation to `dashboard.html`

## Example URL Code Usage

1. **Admin creates code**: `WELCOME2024` with title "Welcome New Users"
2. **Share with users**: Send via email, messaging, or social media
3. **Users access**: Visit `access.html` and enter `WELCOME2024`
4. **Validation**: System checks expiry and usage limits
5. **Access granted**: Users can proceed to main system
6. **Usage tracked**: Admin can see how many times code was used

## 🚀 **Quick Start - Make It Shareable**

### **Option 1: Local Testing (Same Network)**
1. **Run Local Server**: `python start_local_server.py`
2. **Get Network URL**: Share `http://your-ip:8000` with others on your network
3. **Test System**: All features work locally

### **Option 2: Web Hosting (Worldwide Access)**
1. **Choose Platform**: GitHub Pages (free), Netlify, or Vercel
2. **Upload Files**: All HTML, CSS, and JS files
3. **Get Public URL**: Your system accessible worldwide
4. **Configure Dashboard**: Set website URL in admin panel

**📖 See `WEB_HOSTING_GUIDE.md` for detailed hosting instructions**

## 🔗 **Sharing Your System**

### **Before Hosting (Local Only):**
- ✅ Works on your computer
- ✅ Works on same network
- ❌ Not accessible worldwide
- ❌ Links won't work for others

### **After Hosting (Worldwide):**
- ✅ Accessible from anywhere
- ✅ Clickable shareable links
- ✅ Professional appearance
- ✅ Works on all devices
