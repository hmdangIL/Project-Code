<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Science Realm</title>
        <link rel="icon" type="image/x-icon" href="../assets/favicon.jpg" />
        <!-- Font Awesome icons (free version)-->
        <script src="https://use.fontawesome.com/releases/v5.15.4/js/all.js" crossorigin="anonymous"></script>
        <!-- Google fonts-->
        <link href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic" rel="stylesheet" type="text/css" />
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800" rel="stylesheet" type="text/css" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="../css/styles.css" rel="stylesheet" />
        <link href="../css/preloader.css" rel="stylesheet" />
    </head>
    <body>
        <!-- Navigation-->
        <nav class="navbar navbar-expand-lg navbar-light" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="../index.html">Science Realm</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    Menu
                    <i class="fas fa-bars"></i>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto py-4 py-lg-0">
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="../index.html">Home</a></li>
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="../about.html">About</a></li>
                        <li class="nav-item"><a class="nav-link active px-lg-3 py-3 py-lg-4" href="../post_accueil.html">Article</a></li>
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="../contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <!-- Page Header-->
        <header class="masthead" style="background-image: url('../assets/img/img post/dailyfact-bg.jpg')">
            <div class="container position-relative px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-md-10 col-lg-8 col-xl-7">
                        <div class="page-heading">
                            <h1>Daily Facts</h1>
                            <span class="subheading">Don't go around saying the world owes you a living; the world owes you nothing; it was here first.</span>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <!-- Section-->
        <!-- <div class="container">
            <div class="row post-preview">
                <div id="post_3" class="col-md-8 offset-md-2">
                    <a href="post_3.html">
                        <h3 class="title">The harmful effects of radioactive substances</h3>
                        <h4 class="subtitle">If you eat 20000 bananas at once, you will die from radiation instead of dying from choking or a broken stomach.</h4>
                        <span class="meta">
                            Posted by Science Realm on Août 4, 2019
                        </span>
                    </a>
                    <hr class="my-4" />                   
                </div>
            </div>
        </div> -->

        <?php
            require "post_database.php";
            $db = Database::connect();
            $statement = $db->query("SELECT * 
                                    FROM post WHERE post.category1=6 OR post.category2=6 OR post.category3=6 OR post.category4=6 OR post.category5=6 OR post.category6=6
                                    ORDER BY post.id DESC");
            while ($post = $statement->fetch()){
                echo '<div class="container">';
                echo '<div class="row post-preview">';
                    echo '<div class="col-md-8 offset-md-2">';
                        echo '<a href="post_form.php?id='.$post['id'].'">';
                            echo '<h3 class="title">'.$post['title'].'</h3>';
                            echo '<h4 class="subtitle">'.$post['subtitle'].'</h4>';
                            echo '<span class="meta">';
                                echo 'Posted by Science Realm on '.$post['month'].' '.$post['date'].', '.$post['year'];
                            echo '</span>';
                        echo '</a>';
                        echo '<hr class="my-4" />';            
                    echo '</div>';
                echo '</div>';
            echo '</div>';
            }
            Database::disconnect();
        ?>


        <!-- Footer-->
        <footer class="border-top" id="footer">
            <div class="container text-center px-4 px-lg-5">
                <h2 class="text-muted">
                    SCIENCE REALM
                </h2>
                <h5>
                    A scientific newspaper page built by vietnamese students from all over the world
                </h5>
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-md-10 col-lg-8 col-xl-7">
                        <ul class="list-inline text-center">
                            <li class="list-inline-item">
                                <a href="#!">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                            <li class="list-inline-item">
                                <a href="https://www.facebook.com/ScienceRealm/">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                            <li class="list-inline-item">
                                <a href="#!">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                        </ul>
                        <div class="small text-center text-muted fst-italic">Copyright &copy; Design by Ba Duong PHAM 2022. All Rights Reserved</div>
                    </div>
                </div>
            </div>
        </footer>
        
        <!-- Back to top button -->
        <button type="button" class="btn btn-floating btn-lg" id="btn-back-to-top">
            <i class="fas fa-arrow-up"></i>
        </button>

        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="../js/scripts.js"></script>
        <script src="../js/preloader.js"></script>
            
    </body>


        