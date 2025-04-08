from django.db import models

class HeroSection(models.Model):
    # Image for the hero portrait
    portrait_image = models.ImageField(upload_to='Media/', help_text='Upload a portrait image for the hero section.')

    # Content for the hero section
    greeting = models.CharField(max_length=255, help_text='Greeting message, e.g., "Namasté, I\'m"')
    name = models.CharField(max_length=255, help_text='Name to display in the hero section.')
    profession = models.CharField(max_length=255, help_text='Profession or title, e.g., "Frontend Developer"')
    tagline = models.TextField(help_text='Tagline or description for the hero section.')

    # Social media links
    github_link = models.URLField(blank=True, null=True, help_text='Link to GitHub profile.')
    twitter_link = models.URLField(blank=True, null=True, help_text='Link to Twitter profile.')
    instagram_link = models.URLField(blank=True, null=True, help_text='Link to Instagram profile.')
    youtube_link = models.URLField(blank=True, null=True, help_text='Link to YouTube channel.')
    linkedin_link = models.URLField(blank=True, null=True, help_text='Link to LinkedIn profile.')
    discord_link = models.URLField(blank=True, null=True, help_text='Link to Discord server.')

    # Contact and portfolio section
    contact_link = models.URLField(help_text='Link to the contact section.')
    portfolio_link = models.URLField(help_text='Link to the portfolio section.')
    resume_file = models.FileField(upload_to='resumes/', blank=True, null=True, help_text='Upload your resume.')



    def __str__(self):
        return f'Hero Section - {self.name}'

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(help_text="Project URL")
    
    # Store Google Drive File ID instead of full URL
    icon_drive_id = models.CharField(max_length=100, help_text="Google Drive File ID for the project icon")
    banner_drive_id = models.CharField(max_length=100, help_text="Google Drive File ID for the project banner")
    
    stacks = models.CharField(max_length=255, blank=True, null=True)  # Technology stacks used

    @property
    def icon_url(self):
        """Generate direct Google Drive image URL for embedding"""
        if self.icon_drive_id:
            return f"https://lh3.googleusercontent.com/d/{self.icon_drive_id}=s500"  # Adjust `s500` for size
        return ""

    @property
    def banner_url(self):
        """Generate direct Google Drive image URL for embedding"""
        if self.banner_drive_id:
            return f"https://lh3.googleusercontent.com/d/{self.banner_drive_id}=s1000"  # Adjust `s1000` for size
        return ""

    def __str__(self):
        return self.title

    
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_drive_id = models.CharField(max_length=100, null=True,blank=True,help_text="Google Drive File ID for the course image")
    url = models.URLField()
    tag = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        """Generate a direct image URL from Google Drive File ID."""
        if self.image_drive_id:
            return f"https://lh3.googleusercontent.com/d/{self.image_drive_id}=s1000"
        return ""

class AboutMe(models.Model):
    portrait = models.ImageField(upload_to='Media/about_me/', help_text='Upload a portrait image')
    bio = models.TextField(help_text='Write your biography here')

    def __str__(self):
        return "About Me Section"

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

class Skill(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the skill')
    icon_url = models.URLField(help_text='URL of the skill icon (e.g., Icons8 link)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

class College(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class Organizer(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class EventList(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300, null=True, blank=True)
    

    # Store Google Drive File ID instead of local image upload
    image_drive_id = models.CharField(max_length=100, blank=True,null=True,help_text="Google Drive File ID for certificate image")

    tag = models.CharField(max_length=50, blank=True, null=True)  # e.g., Symposium, Hackathon
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True, blank=True)
    organizer = models.ForeignKey(Organizer, on_delete=models.SET_NULL, null=True, blank=True)
    won_prize = models.CharField(max_length=50, blank=True, null=True)  # e.g., "1st Place", "2nd Runner-Up"

    event_type = models.ForeignKey(EventList,default=1, on_delete=models.SET_NULL, null=True, blank=True)  # Type of event

    issued_date = models.DateField(blank=True, null=True)  # Date issued
    level = models.CharField(
        max_length=50, choices=[
            ("College", "College"),
            ("National", "National"),
            ("International", "International"),
        ],
        blank=True, null=True
    )  # Competition level

    category = models.CharField(
        max_length=50, choices=[
            ("Technical", "Technical"),
            ("Non-Technical", "Non-Technical"),
        ],
        blank=True, null=True
    )  # Skill-based category

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        """Generate a public Google Drive image link from the file ID."""
        if self.image_drive_id:
            return f"https://lh3.googleusercontent.com/d/{self.image_drive_id}=s1000"
        return ""


