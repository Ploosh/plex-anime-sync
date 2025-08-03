"use client"

import { LogIn, LogOut, Settings, User, UserCircle } from "lucide-react"
import { useState } from "react"

import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export function AccountDropdown() {
  // TODO: Replace with actual authentication state management
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const handleProfile = () => {
    // TODO: Navigate to profile page
    console.log("Navigate to profile")
  }

  const handleSettings = () => {
    // TODO: Navigate to settings page
    console.log("Navigate to settings")
  }

  const handleLogout = () => {
    // TODO: Implement logout logic
    setIsLoggedIn(false)
    console.log("User logout")
  }

  const handleSignIn = () => {
    // TODO: Implement sign in logic
    setIsLoggedIn(true)
    console.log("User sign in")
  }

  // If user is not logged in, show sign in button
  if (!isLoggedIn) {
    return (
      <Button variant="outline" onClick={handleSignIn} className="flex items-center gap-2">
        <LogIn className="h-4 w-4" />
        <span>Sign In</span>
      </Button>
    )
  }

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" size="icon">
          <UserCircle className="h-[1.2rem] w-[1.2rem]" />
          <span className="sr-only">Account menu</span>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <DropdownMenuItem onClick={handleProfile}>
          <User className="mr-2 h-4 w-4" />
          Profile
        </DropdownMenuItem>
        <DropdownMenuItem onClick={handleSettings}>
          <Settings className="mr-2 h-4 w-4" />
          Account Settings
        </DropdownMenuItem>
        <DropdownMenuSeparator />
        <DropdownMenuItem onClick={handleLogout}>
          <LogOut className="mr-2 h-4 w-4" />
          Sign Out
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
