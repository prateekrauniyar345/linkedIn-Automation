<template>
    <div>
        <header 
          class="header-container"
        >
            <!-- logo -->
            <div>
                <div 
                  class="d-flex flex-column align-items-center text-center"
                  onclick="window.location.href='/'"
                  style="cursor: pointer;"
                >
                    <div class="logo"></div>
                    <p style="font-size: 18px;">OCTOPUS</p>
                </div>
            </div>

            <!-- navigation -->
            <nav class="header-nav">
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </nav>

            <!-- user actions -->
            <div class="header-actions">
                <button class="login-btn-style" @click="signin">Sign In</button>
                <button class="login-btn-style" @click="signup">Sign Up</button>
            </div>
        </header>
    </div>
</template>


<script setup lang="ts">
    const signin = () => {
        window.location.href = '/signin';
    }
    const signup = () => {
        window.location.href = '/signup';
    }
</script>


<style>
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.2rem 1.5rem;
        background-color: #ffffff;
    }

    .logo {
        width: 70px;     
        height: 70px;    
        background-image: url('/icons/Project.svg');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
    }

    nav ul {
        list-style: none;
        margin: 0;
        padding: 0;
        display: flex;
        gap: 3rem;
        align-items: center;
    }

    nav ul li a {
        text-decoration: none;
        color: #333;
        font-weight: 500;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        position: relative;
    }

    nav ul li a:hover {
        color: #5c4176;
    }

    nav ul li a::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 0;
        height: 2px;
        background-color: #5c4176;
        transition: width 0.3s ease;
    }

    nav ul li a:hover::after {
        width: 100%;
    }

    .header-actions {
        display: flex;
        gap: 1.5rem;
        align-items: center;
    }

    .login-btn-style {
        padding: 0.8rem 1.8rem;
        font-size: 1rem;
        font-weight: 600;
        border: 2px solid #5c4176;
        border-radius: 8px;
        background-color: white;
        color: #5c4176;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
    }

    .login-btn-style:hover {
        background-color: #5c4176;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(92, 65, 118, 0.3);
    }

    .login-btn-style:active {
        transform: translateY(0);
    }
</style>