using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using IWPandDatabase.Models;
using System.Web.Security;
using System.Data.SqlClient;
using System.Data;

namespace IWPandDatabase.Controllers
{
    public class HomeController : Controller
    {
        public static string UserName;
        BlockChain db = new BlockChain();
        // GET: Home
        [Authorize]
        public ActionResult Index()
        {
            return View();
        }
        [HttpGet]
        public ActionResult SignUp()
        {
            return View();
        }
        [HttpPost]
        public ActionResult SignUp(Users user)
        {
            if (db.Users.Any(x => x.UserName == user.UserName)|| db.Users.Any(x => x.Email == user.Email)|| db.Users.Any(x => x.PhoneNumber == user.PhoneNumber))
            {
                ViewBag.Notification = "This Account Already existed";
                return View();
            }
            else
            {
                db.Users.Add(user);
                db.SaveChanges();
                Session["UserID"] = user.UserID.ToString();
                Session["UserName"] = user.UserName.ToString();
                return RedirectToAction("Index", "Home");

            }
            
        }
        [HttpGet]
        public ActionResult Login()
        {
            return View();
        }
        
        [HttpPost]
        public ActionResult Login(Users user)
        {
            var checkLogin = db.Users.Where(x => x.UserName.Equals(user.UserName) && x.Password.Equals(user.Password)).FirstOrDefault();
            if(checkLogin!=null)
            {
                UserName = user.UserName;
                Session["UserID"] = user.UserID.ToString();
                Session["UserName"] = user.UserName.ToString();
                FormsAuthentication.SetAuthCookie(checkLogin.UserName, false);
                return RedirectToAction("Index", "Home");
            }
            else
            {
                ViewBag.Notification = "Wrong UserName or Password";
            }
            return View();
        }
        public ActionResult Logout()
        {
            Session.Clear();
            return RedirectToAction("Index", "Home");
        }
        [HttpGet]
        [Authorize]
        public ActionResult Keys()
        {
            return View();
        }
        [HttpPost]
        public ActionResult Keys(Key key,Users user)
        {
            if (Request.HttpMethod == "POST")
            {
                using (SqlConnection con = new SqlConnection("Data Source=KARFELIN;Integrated Security=true;Initial Catalog=BlockChain1"))
                {
                    using (SqlCommand cmd = new SqlCommand("KeyHash", con))
                    {
                        db.Users.Any(x => x.UserName == user.UserName);
                        cmd.CommandType = CommandType.StoredProcedure;
                        cmd.Parameters.AddWithValue("@UserName",UserName);
                        cmd.Parameters.AddWithValue("@PublicKey", key.PublicKey);
                        cmd.Parameters.AddWithValue("@PrivateKey", key.PrivateKey);
                        con.Open();
                        ViewData["result"] = cmd.ExecuteNonQuery();
                        con.Close();
                    }

                }
            }
            return View();
        }
        [HttpGet]
        [Authorize]
        public ActionResult Transaction()
        {
            using (SqlConnection con = new SqlConnection("Data Source=KARFELIN;Integrated Security=true;Initial Catalog=BlockChain1"))
            {
                using (SqlCommand cmd2 = new SqlCommand("verify", con))
                {
                    con.Open();
                    cmd2.CommandType = CommandType.StoredProcedure;
                    ViewData["result"] = cmd2.ExecuteNonQuery();
                    con.Close();
                }
                using (SqlCommand cmd1 = new SqlCommand("trnsVerify", con))
                {
                    con.Open();
                    cmd1.CommandType = CommandType.StoredProcedure;
                    cmd1.Parameters.AddWithValue("@UserName", UserName);
                    ViewData["result"] = cmd1.ExecuteNonQuery();
                    con.Close();
                }
            }
                return View();
        }
        [HttpPost]
        public ActionResult Transaction(Transaction trns)
        {
            if (Request.HttpMethod == "POST")
            {

                using (SqlConnection con = new SqlConnection("Data Source=KARFELIN;Integrated Security=true;Initial Catalog=BlockChain1"))
                {
                    SqlCommand cmd1 = new SqlCommand("publicKey", con);
                    con.Open();
                    cmd1.CommandType = CommandType.StoredProcedure;
                    con.Close();

                    using (SqlCommand cmd = new SqlCommand("Transfer", con))
                    {
                        con.Open();
                        cmd.CommandType = CommandType.StoredProcedure;
                        cmd.Parameters.AddWithValue("@amount", trns.Message);
                        cmd.Parameters.AddWithValue("@SentTo", trns.Sent);
                        cmd.Parameters.AddWithValue("@SentFrom", trns.Sender);
                        cmd.Parameters.AddWithValue("@PrivateKey", trns.PrivateKey);
                        cmd.Parameters.AddWithValue("@signature", trns.MessageSignature);
                        cmd.Parameters.AddWithValue("@UserName",UserName );
                        ViewData["result"] = cmd.ExecuteNonQuery();
                        con.Close();
                    }
                }
            }
            return View();

        }
        [HttpGet]
        [Authorize]
        public ActionResult Blocks()
        {
            return View();
        }
        [HttpPost]
        public ActionResult Blocks(Blocks block)
        {
            using (SqlConnection con = new SqlConnection("Data Source=KARFELIN;Integrated Security=true;Initial Catalog=BlockChain1"))
            {
                using (SqlCommand cmd = new SqlCommand("BlockAdd", con))
                {
                    con.Open();
                    cmd.CommandType = CommandType.StoredProcedure;
                    cmd.Parameters.AddWithValue("@UserName", UserName);
                    cmd.Parameters.AddWithValue("@Blockid", block.BlockID);
                    cmd.Parameters.AddWithValue("@nonce", block.Nonce);
                    cmd.Parameters.AddWithValue("@data", block.Data);
                    cmd.Parameters.AddWithValue("@hash", block.Hash);
                    ViewData["result"] = cmd.ExecuteNonQuery();
                    con.Close();
                }
            }
            return View();
        }
        [HttpGet]
        [Authorize]
        public ActionResult BlockChain()
        {
           
            return View();
        }

        [HttpPost]
        public ActionResult BlockChain(BlockChains bc)
        {
            using (SqlConnection con = new SqlConnection("Data Source=KARFELIN;Integrated Security=true;Initial Catalog=BlockChain1"))
            {
                using (SqlCommand cmd = new SqlCommand("chain", con))
                {
                    con.Open();
                    cmd.CommandType = CommandType.StoredProcedure;
                    cmd.Parameters.AddWithValue("@UserName", UserName);
                    cmd.Parameters.AddWithValue("@Blockid", bc.BlockID);
                    cmd.Parameters.AddWithValue("@nonce", bc.Nonce);
                    cmd.Parameters.AddWithValue("@data", bc.Data);
                    cmd.Parameters.AddWithValue("@prev", bc.Prev);
                    cmd.Parameters.AddWithValue("@hash", bc.Hash);
                    ViewData["result"] = cmd.ExecuteNonQuery();
                    con.Close();
                }
            }
            return View();
        }
    }
}